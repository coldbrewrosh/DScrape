/*<!--*/
(function() {
    var qss = "&cb=" + Math.floor(99999999999 * Math.random());
    try {
        qss += "&ref=" + encodeURIComponent(document.referrer)
    } catch (e) {}
    try {
        qss += "&sc_r=" + encodeURIComponent(screen.width + "x" + screen.height)
    } catch (e) {}
    try {
        qss += "&sc_d=" + encodeURIComponent(screen.colorDepth.toString())
    } catch (e) {}
    var callDis = function(e, t, n, o) {
            function c() {
                s
                callDisInternal(e, t, n, o)
            }
            "complete" === document.readyState ? setTimeout(c) : window.addEventListener ? window.addEventListener("load", c, !1) : window.attachEvent("onload", c)
        },
        disCalled = !1,
        callDisInternal = function(e, t, n, o) {
            disCalled || (disCalled = !0, n = (n ? "https:" : "") + "//" + t + "/dis/dis.aspx", (t = document.createElement("iframe")).width = t.height = "0", t.style.display = "none", t.title = "Criteo DIS iframe", void 0 !== o && "" !== o && (document.body.appendChild(t), null != t.contentDocument) ? (t.contentDocument.open(), t.contentDocument.write(o), t.contentDocument.close()) : (t.src = (n + "?p=" + e + qss).substring(0, 2e3), (o = document.getElementById("criteoTagsContainer")) ? (o.appendChild(t), "undefined" != typeof criteo_q && "function" == typeof criteo_q.removeLater && criteo_q.removeLater(t)) : criteo_q.push({
                event: "appendTag",
                element: t
            })))
        };
    qss += '&idcpy=68f753ff-ff62-4718-9d6c-850ae5296df7';
    callDis(46853, 'widget.as.criteo.com', true, '<!DOCTYPE html><html lang=\"en\"><head><title>Dising<\/title><script  type=\"text\/javascript\">rD = false;function edcTimeout() {rD = true; }function cto_AI(u,n) { if (rD) {return;} var cto_ifr=document.getElementById(\'cto_sub_ifr_px\');var cto_ifr_doc=null;if(typeof(cto_ifr)===\'undefined\'||cto_ifr==null)cto_ifr_doc=document;else if(cto_ifr.contentDocument)cto_ifr_doc=cto_ifr.contentDocument;else if(cto_ifr.contentWindow)cto_ifr_doc=cto_ifr.contentWindow.document;else if(cto_ifr.document)cto_ifr_doc=cto_ifr.document;else cto_ifr_doc=document;if(cto_ifr_doc.createElement){var im=cto_ifr_doc.createElement(\'IMG\');if(im){var d=document.getElementById(\'cto_pc\');if(d!==null && d.appendChild){d.appendChild(im)}if(n){im.onload=n;im.onerror=n;im.onabort=n}im.src=u}} }function cto_l(){if(typeof(cto_loaded)===\'undefined\')cto_loaded=1;else cto_loaded++;}function cto_run() {function l_i1_1(){cto_AI(\'https:\/\/cm.g.doubleclick.net\/pixel?google_nid=cjp&google_sc&google_ula=913071&CriteoUserId=k-evGzYYnBg2Yeob4kledrML7HfLUzqByEucZwkQ&google_cm&google_hm=ay1ldkd6WVluQmcyWWVvYjRrbGVkck1MN0hmTFV6cUJ5RXVjWndrUQ\', cto_l);}function l_i2_1(){cto_AI(\'https:\/\/x.bidswitch.net\/sync?dsp_id=46&user_id=k-LRRT0YnBg2Yeob4kledrML7HfLW4qD9-C7Fcpw&expires=30\', cto_l);}function l_i3_1(){cto_AI(\'https:\/\/ib.adnxs.com\/getuid?https:\/\/dis.criteo.com\/dis\/rtb\/appnexus\/cookiematch.aspx?appnxsid=$UID\', l_i3_2);}function l_i3_2(){cto_AI(\'https:\/\/ib.adnxs.com\/setuid?entity=52&code=k-QY3fGYnBg2Yeob4kledrML7HfLU6wr9Xvas2iA\', cto_l);}function l_i4_1(){cto_AI(\'https:\/\/contextual.media.net\/cksync.php?cs=3&type=crt&ovsid=k-cwjd0InBg2Yeob4kledrML7HfLWasPUVRM_icw\', cto_l);}function l_i5_1(){cto_AI(\'https:\/\/pixel.rubiconproject.com\/tap.php?v=6434&nid=2149&put=k-FnqQE4nBg2Yeob4kledrML7HfLVmNJ_FnWaQfg&expires=30\', cto_l);}function l_i6_1(){cto_AI(\'https:\/\/rtb-csync.smartadserver.com\/redir\/?partnerid=79&partneruserid=k-Vvi94onBg2Yeob4kledrML7HfLUoi_aBnxmJOg\', cto_l);}function l_i7_1(){cto_AI(\'https:\/\/sync-t1.taboola.com\/sg\/criteortb-network\/1\/rtb-h\/?taboola_hm=k-UPzzmInBg2Yeob4kledrML7HfLWlieu67aaW9Q\', cto_l);}function l_i8_1(){cto_AI(\'https:\/\/criteo-sync.teads.tv\/um?eid=80&uid=k-TXY9B4nBg2Yeob4kledrML7HfLW3i1mJuIWWxw\', cto_l);}function l_i9_1(){cto_AI(\'https:\/\/eb2.3lift.com\/xuid?mid=2711&xuid=k-1ACR_InBg2Yeob4kledrML7HfLXmTIzqiqLAsw&dongle=013b\', cto_l);}function l_i10_1(){cto_AI(\'https:\/\/ups.analytics.yahoo.com\/ups\/58301\/sync?_origin=1&uid=k-y39EJYnBg2Yeob4kledrML7HfLUTc14lzEtNkw\', l_i10_2);}function l_i10_2(){cto_AI(\'https:\/\/ups.analytics.yahoo.com\/ups\/58301\/sync?_origin=0&redir=true&uid=k-y39EJYnBg2Yeob4kledrML7HfLUTc14lzEtNkw\', cto_l);}function l_i11_1(){cto_AI(\'https:\/\/adgen.socdm.com\/rtb\/sync?proto=adgen&dspid=23\', cto_l);}function l_i12_1(){cto_AI(\'https:\/\/tg.socdm.com\/aux\/idsync?proto=criteo&dsp_uid=k-B9tmJInBg2Yeob4kledrML7HfLXZvAgwpaBxdQ\', cto_l);}function l_i13_1(){cto_AI(\'https:\/\/gum.criteo.com\/sync?c=4&r=1&a=1&u=https:\/\/tags.bluekai.com\/site\/29001\/sync?3rdpartyuserid=%40USERID%40\', l_i13_2);}function l_i13_2(){cto_AI(\'https:\/\/gum.criteo.com\/sync?c=83&r=1&a=1&u=https%3A%2F%2Fbeacon.krxd.net%2Fusermatch.gif%3Fpartner%3Dcriteo%26partner_uid%3D%40USERID%40\', cto_l);}function l_i14_1(){cto_AI(\'https:\/\/r.casalemedia.com\/rum?cm_dsp_id=20&external_user_id=k-yTclf4nBg2Yeob4kledrML7HfLXdnrVIthJfUw\', cto_l);}function l_i15_1(){cto_AI(\'https:\/\/adx.dable.io\/pixel?dsp_id=6&uid=k-eQZvLYnBg2Yeob4kledrML7HfLUaSWgdcckabtJx080B9W9M\', cto_l);}function l_i16_1(){cto_AI(\'https:\/\/cs.adingo.jp\/sync\/?from=criteo&id=k-uLHVUonBg2Yeob4kledrML7HfLWe-wm-umMZGQ\', cto_l);}function l_i17_1(){cto_AI(\'https:\/\/ads.stickyadstv.com\/user-registering?dataProviderId=434&userId=k-BiDTXonBg2Yeob4kledrML7HfLVY3Su9jxm2hg\', cto_l);}function l_i18_1(){cto_AI(\'https:\/\/ad.360yield.com\/match?publisher_dsp_id=38&external_user_id=k-FAEfRYnBg2Yeob4kledrML7HfLWqp0Xy9HI38A\', cto_l);}function l_i19_1(){cto_AI(\'https:\/\/idsync.rlcdn.com\/362338.gif?partner_uid=k-6o034onBg2Yeob4kledrML7HfLURkdfgyXDtlg\', cto_l);}function l_i20_1(){cto_AI(\'https:\/\/exchange.mediavine.com\/usersync\/push?partner=criteo&partnerId=k-Jb-wIInBg2Yeob4kledrML7HfLVnlbH6FKhp7Gk1CD_dEf8U\', cto_l);}function l_i21_1(){cto_AI(\'https:\/\/c.bing.com\/c.gif?Red3=CTOMS_pd&cbid=k-UXvjVInBg2Yeob4kledrML7HfLVEgPvoRxfzCAgQQHk_tIOP\', cto_l);}function l_i22_1(){cto_AI(\'https:\/\/sync.outbrain.com\/cookie-sync?p=criteo&uid=k-ZFO0o4nBg2Yeob4kledrML7HfLVqtRDfqjxCUw&initiator=partner\', cto_l);}function l_i23_1(){cto_AI(\'https:\/\/simage2.pubmatic.com\/AdServer\/Pug?vcode=bz0yJnR5cGU9MSZjb2RlPTE5MjgmdGw9NDMyMDA=&piggybackCookie=uid:k-ln0wX4nBg2Yeob4kledrML7HfLXBZWjjIzpQcw\', cto_l);}function l_i24_1(){cto_AI(\'https:\/\/s.ad.smaato.net\/c\/?dspInit=1001851&dspCookie=k-cHFurInBg2Yeob4kledrML7HfLUXxz0bwaBGQA\', cto_l);}function l_i25_1(){cto_AI(\'https:\/\/ade.clmbtech.com\/uid\/sync.htm?pid=13079&cuid=k-8m6U54nBg2Yeob4kledrML7HfLWeQEboeojrFg\', cto_l);}function l_i26_1(){cto_AI(\'https:\/\/sync-criteo.ads.yieldmo.com\/sync?id=k-yRZpVInBg2Yeob4kledrML7HfLVW5sz7jjeZvQ&pn_id=criteo&ext=1\', cto_l);}cto_tot = 26;l_i1_1();l_i2_1();l_i3_1();l_i4_1();l_i5_1();l_i6_1();l_i7_1();l_i8_1();l_i9_1();l_i10_1();l_i11_1();l_i12_1();l_i13_1();l_i14_1();l_i15_1();l_i16_1();l_i17_1();l_i18_1();l_i19_1();l_i20_1();l_i21_1();l_i22_1();l_i23_1();l_i24_1();l_i25_1();l_i26_1();}<\/script><\/head><body><iframe id=\"cto_sub_ifr_px\" src=\"about:blank\" style=\"width:1px;height:1px;display:none;\"><div id=\'cto_pc\' style=\'display:none\'><\/div><\/iframe><script  type=\"text\/javascript\">document.body.onload = function(){ if(window.cto_run) cto_run(); };window.setTimeout(function(){ if(typeof(cto_loaded)===\'undefined\' || cto_loaded<cto_tot) {edcTimeout();var redirectLocation=location.protocol+\'\/\/static.criteo.net\/empty.html\'; location.replace(redirectLocation);}}, 5000);<\/script><\/body><\/html>');
})();


(function() {
    var CRITEO_COM_TOKEN = "AwnOWg2dzaxHPelVjqOT/Y02cSxnG2FkjXO7DlX9VZF0eyD0In8IIJ9fbDFZGXvxNvn6HaF51qFHycDGLOkj1AUAAACAeyJvcmlnaW4iOiJodHRwczovL2NyaXRlby5jb206NDQzIiwiZmVhdHVyZSI6IlByaXZhY3lTYW5kYm94QWRzQVBJcyIsImV4cGlyeSI6MTY5NTE2Nzk5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0=",
        addTrialToken = function(e) {
            var t = document.createElement("meta");
            t.httpEquiv = "origin-trial", t.content = e, document.head.appendChild(t)
        },
        tokenAdded = function() {
            for (var e = 0, t = document.getElementsByTagName("meta"); e < t.length; e++) {
                var n = t[e];
                if ("origin-trial" === n.httpEquiv && n.content === CRITEO_COM_TOKEN) return !0
            }
            return !1
        },
        isChrome = function() {
            return !!window.chrome
        };
    isChrome() && !tokenAdded() && addTrialToken(CRITEO_COM_TOKEN);
    var onLoad = function(e) {
            "complete" === document.readyState ? setTimeout(e) : window.addEventListener ? window.addEventListener("load", e, !1) : window.attachEvent("onload", e)
        },
        dropIframe = function(e, t) {
            var o;
            (!true || "joinAdInterestGroup" in navigator) && ((o = document.createElement("iframe")).allow = "join-ad-interest-group", o.width = o.height = "0", o.style.display = "none", o.title = t, o.src = e, document.body.appendChild(o), "undefined" != typeof criteo_q && "function" == typeof criteo_q.removeLater ? criteo_q.removeLater(o) : setTimeout(function() {
                document.body.removeChild(o)
            }, 3e4))
        },
        callFledge = function(e, t, o, d, n) {
            var i = e + "/tagging/advertiser" + "?partnerId=" + t + "&uid=" + d;
            o && (i += "&fpId=" + o), n && (i += "&requestId=" + n), onLoad(function() {
                isChrome() && dropIframe(i, "Criteo Fledge iframe")
            })
        };
    callFledge('https://fledge.as.criteo.com', 46853, '', '68f753ff-ff62-4718-9d6c-850ae5296df7', 'f99286b3-3632-4ac2-a111-191c70f7fa06');
})();

(function() {
    var CRITEO_COM_TOKEN = "AwnOWg2dzaxHPelVjqOT/Y02cSxnG2FkjXO7DlX9VZF0eyD0In8IIJ9fbDFZGXvxNvn6HaF51qFHycDGLOkj1AUAAACAeyJvcmlnaW4iOiJodHRwczovL2NyaXRlby5jb206NDQzIiwiZmVhdHVyZSI6IlByaXZhY3lTYW5kYm94QWRzQVBJcyIsImV4cGlyeSI6MTY5NTE2Nzk5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0=",
        addTrialToken = function(e) {
            var t = document.createElement("meta");
            t.httpEquiv = "origin-trial", t.content = e, document.head.appendChild(t)
        },
        tokenAdded = function() {
            for (var e = 0, t = document.getElementsByTagName("meta"); e < t.length; e++) {
                var n = t[e];
                if ("origin-trial" === n.httpEquiv && n.content === CRITEO_COM_TOKEN) return !0
            }
            return !1
        },
        isChrome = function() {
            return !!window.chrome
        };
    isChrome() && !tokenAdded() && addTrialToken(CRITEO_COM_TOKEN);
    var isFeatureAllowed = function(i) {
            var e = document.featurePolicy;
            return !(!e || !e.features()) && e.features().some(function(e) {
                return e === i
            })
        },
        callARA = function(e, i, t, r, n, o, a, u, l, d) {
            e = e + "/register-trigger" + "?partner_id=" + i + "&uid=" + t + "&event_name=" + r + "&islcc=" + (n ? 1 : 0) + "&amount_local=" + a + "&amount_euro=" + u + o.map(function(e) {
                return "&hashed_ext_id=" + e
            }).join("") + "&client_side_event_id=" + l + ("" === d ? "" : "&transaction_id=" + d);
            isChrome() && isFeatureAllowed("attribution-reporting") && window.fetch(e, {
                keepalive: !0,
                credentials: "include",
                attributionReporting: {
                    eventSourceEligible: !1,
                    triggerEligible: !0
                }
            })
        };
    callARA('https://measurement-api.criteo.com', 46853, '68f753ff-ff62-4718-9d6c-850ae5296df7', 'Listing', false, [], 0, 0, 'fd88c0fd-2422-488d-a131-6b63fb302d87', '');
})();

/*-->*/