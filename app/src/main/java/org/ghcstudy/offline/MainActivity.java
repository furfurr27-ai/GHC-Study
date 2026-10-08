package org.ghcstudy.offline;

import android.app.Activity;
import android.os.Build;
import android.os.Bundle;
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
    private WebView webView;
    private boolean backPending;

    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        webView = new WebView(this);
        webView.setWebViewClient(new WebViewClient());
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
        // Prefer app-provided navigation when present; do not overwrite view/mode
        // globals with hard-coded guesses. Modal dismissal is safe and reversible.
        final String script = "(function(){try{"
                + "if(typeof window.ghcGoBack==='function'){return window.ghcGoBack()?'handled':'root';}"
                + "var m=document.getElementById('modal');"
                + "if(m&&!m.classList.contains('hidden')){"
                + "var c=document.getElementById('closeModal');"
                + "if(c){c.click();return 'handled';}}"
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
