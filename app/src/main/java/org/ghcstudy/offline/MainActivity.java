package org.ghcstudy.offline;

import android.app.Activity;
import android.os.Bundle;
import android.os.Build;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebSettings;
import android.window.OnBackInvokedDispatcher;

public class MainActivity extends Activity {
    private WebView webView;

    @Override public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        webView = new WebView(this);
        webView.setWebViewClient(new WebViewClient());
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setAllowFileAccess(true);
        setContentView(webView);
        webView.loadUrl("file:///android_asset/index.html");

        if (Build.VERSION.SDK_INT >= 33) {
            getOnBackInvokedDispatcher().registerOnBackInvokedCallback(
                OnBackInvokedDispatcher.PRIORITY_DEFAULT,
                this::navigateBack
            );
        }
    }

    private void navigateBack() {
        if (webView == null) {
            finish();
            return;
        }

        String js = "(function(){try{" +
            "var m=document.getElementById('modal');" +
            "if(m&&!m.classList.contains('hidden')){" +
                "var c=document.getElementById('closeModal');if(c){c.click();return 'handled';}" +
            "}" +
            "var backs=document.querySelectorAll('.backlink,.study-back');" +
            "for(var i=0;i<backs.length;i++){" +
                "var b=backs[i],s=getComputedStyle(b);" +
                "if(s.display!=='none'&&s.visibility!=='hidden'&&b.offsetParent!==null){b.click();return 'handled';}" +
            "}" +
            "if(typeof view!=='undefined'&&view!=='study'){" +
                "view='study';if(typeof mode!=='undefined')mode='home';" +
                "if(typeof render==='function')render();window.scrollTo(0,0);return 'handled';" +
            "}" +
            "if(typeof mode!=='undefined'&&mode!=='home'){" +
                "mode='home';if(typeof render==='function')render();window.scrollTo(0,0);return 'handled';" +
            "}" +
            "return 'root';}catch(e){return 'error';}})();";

        webView.evaluateJavascript(js, value -> {
            if ("\"handled\"".equals(value)) return;
            if (webView.canGoBack()) webView.goBack();
            else finish();
        });
    }

    @Override public void onBackPressed() {
        navigateBack();
    }

    @Override public void onDestroy() {
        if (webView != null) webView.destroy();
        super.onDestroy();
    }
}
