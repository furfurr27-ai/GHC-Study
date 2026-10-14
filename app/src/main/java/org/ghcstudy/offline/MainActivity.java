package org.ghcstudy.offline;

import android.app.Activity;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.webkit.ConsoleMessage;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.window.OnBackInvokedDispatcher;

/**
 * Thin offline WebView host. JavaScript owns in-app navigation; Android owns
 * hardware/system Back, WebView history fallback and activity lifecycle.
 */
public final class MainActivity extends Activity {
    private static final String START_URL = "file:///android_asset/index.html";
    private static final String LOG_TAG = "GHCWebView";
    private WebView webView;
    private boolean backPending;

    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        webView = new WebView(this);
        webView.setWebViewClient(new WebViewClient() {
            @Override public void onPageStarted(WebView view, String url, android.graphics.Bitmap favicon) {
                Log.i(LOG_TAG, "Page start: " + url);
            }
            @Override public void onPageFinished(WebView view, String url) {
                Log.i(LOG_TAG, "Page finished: " + url);
            }
            @Override public void onReceivedError(WebView view, WebResourceRequest request, WebResourceError error) {
                Log.e(LOG_TAG, "WebView load error: " + request.getUrl()
                        + " code=" + error.getErrorCode() + " " + error.getDescription());
            }
        });
        webView.setWebChromeClient(new WebChromeClient() {
            @Override public boolean onConsoleMessage(ConsoleMessage message) {
                Log.i(LOG_TAG, "JS " + message.messageLevel() + " " + message.sourceId()
                        + ":" + message.lineNumber() + " " + message.message());
                return true;
            }
        });
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true); // Existing quiz progress uses DOM storage.
        settings.setAllowFileAccess(true);   // Offline app media uses file URLs.
        settings.setAllowFileAccessFromFileURLs(false);
        settings.setAllowUniversalAccessFromFileURLs(false);
        setContentView(webView);
        if (state == null) {
            webView.loadUrl(START_URL);
        } else {
            webView.restoreState(state);
        }
        if (Build.VERSION.SDK_INT >= 33) {
            getOnBackInvokedDispatcher().registerOnBackInvokedCallback(
                    OnBackInvokedDispatcher.PRIORITY_DEFAULT, this::navigateBack);
        }
    }

    @Override protected void onSaveInstanceState(Bundle state) {
        if (webView != null) webView.saveState(state);
        super.onSaveInstanceState(state);
    }

    private void navigateBack() {
        if (webView == null || backPending) return;
        backPending = true;
        // The app keeps its view/mode variables inside an IIFE. They are not
        // global and cannot be read by evaluateJavascript from the WebView.
        // Use the existing visible controls: their click handlers *do* have
        // access to the closure, preserving the app's own state transitions.
        final String script = "(function(){try{"
                + "var m=document.getElementById('modal');"
                + "if(m&&!m.classList.contains('hidden')){"
                + "var c=document.getElementById('closeModal');"
                + "if(c){c.click();return 'handled';}}"
                + "var x=document.getElementById('studyCatBack');"
                + "if(x){x.click();return 'handled';}"
                + "x=document.getElementById('studyHubBack');"
                + "if(x){x.click();return 'handled';}"
                + "x=document.querySelector('#app [data-action=home]');"
                + "if(x){x.click();return 'handled';}"
                + "var active=document.querySelector('.navbtn.active');"
                + "if(active&&active.getAttribute('data-tab')!=='study'){"
                + "x=document.querySelector('.navbtn[data-tab=study]');"
                + "if(x){x.click();return 'handled';}}"
                + "return 'root';"
                + "}catch(e){return 'error';}})();";
        webView.evaluateJavascript(script, result -> {
            backPending = false;
            if ("\"handled\"".equals(result)) return;
            if (webView != null && webView.canGoBack()) webView.goBack();
            else finish();
        });
    }

    @Override public void onBackPressed() {
        navigateBack();
    }

    @Override protected void onDestroy() {
        if (webView != null) {
            webView.stopLoading();
            webView.destroy();
            webView = null;
        }
        super.onDestroy();
    }
}
