//改变元素背景颜色
;
(function($) {

	/* 
	 * 国内手机号校验
	 */
	$.fn.checkMobile = function() {
		// 移动：134、135、136、137、138、139、150、151、157(TD)、158、159、187、188
		// 　　 联通：130、131、132、152、155、156、185、186
		// 　　 电信：133、153、180、189、（1349卫通
		var mobile = this.val();
		if (!mobile || mobile === '' || mobile === null) {
			return "请输入手机号码";
		}
		return (/^[1]([3][0-9]{1}|59|58|88|89)[0-9]{8}$/.test(this.val())) ? "" : "请输入11位数国内手机号";
	};
	// 获取图形验证码
	// 发送手机短信验证码
	// 联合登陆
	//
	//
	//

	/* 
	 *事件代理（tap特定）
	 *tagNm（绑定特定的tag）
	 *callback 回调函数（事件响应处理方法）
	 */
	$.fn.eventDelegate = function(opts) {
		this.on('tap', function(e) {
			var targetTest = e.target;
			if (!opts.tagNm || targetTest.tagName === opts.tagNm) {
				opts.callback();
			}
		});
	};

	// 跳转url
	$.gotoUrl = function(url) {
		window.location.href=url;
	};

	// 动态加载script
	$.load_script = function (xyUrl, callback) {
        var head = document.getElementsByTagName('head')[0];
        var script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = xyUrl;
        // 借鉴了jQuery的script跨域方法
        script.onload = script.onreadystatechange = function() {
            if ((!this.readyState || this.readyState === "loaded" || this.readyState === "complete")) {
                callback && callback();
                // Handle memory leak in IE
                script.onload = script.onreadystatechange = null;
                if (head && script.parentNode) {
                    head.removeChild(script);
                }
            }
        };
        // Use insertBefore instead of appendChild to circumvent an IE6 bug.
        head.insertBefore(script, head.firstChild);
    };

    // 随机生成函数名
    $.createFunctionName = function(){
    	return  'cbk_' + Math.round(Math.random() * 10000); // 随机函数名
    }

	// 样例
	$.fn.vgoPlugin = function(option) {
		var opts = $.extend({}, $.fn.vgoPlugin.defaults, option);
		this.css('backgroundColor', opts.color);
	};
	$.fn.vgoPlugin.defaults = {
		color: '#f60'
	};
})(Zepto);