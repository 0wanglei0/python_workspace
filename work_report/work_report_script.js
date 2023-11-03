var n = (() => "undefined" != typeof GM_xmlhttpRequest ? GM_xmlhttpRequest : void 0)();

function i() {
    var t;
    return (null == (t = document.querySelector("#loggedas a")) ? void 0 : t.textContent) ?? ""
}

function s(t) {
    if ("xuhui" === i()) return !0;
    const e = localStorage.getItem(`enhance_${t}`);
    return !e || JSON.parse(e)
}

function r() {
    o(), function () {
        const t = document.querySelector("#top-menu");
        if (t) {
            const n = document.createElement("span");
            n.textContent = "插件设置", n.classList.add("float-right", "mr-4", "cursor-pointer", "select-none"), n.addEventListener("click", (() => {
                e.fire({template: "#plugin_config_template"}).then((() => {
                    window.location.reload();
                })), l("my_page_config"), l("issues_config"), l("member_list_config"), l("eggshell_config");
            }));
            const i = document.createElement("template");
            i.id = "plugin_config_template", i.innerHTML = '\n      <swal-title>Redmine插件设置</swal-title>\n      <swal-html>\n      <div class="form-control w-52">\n        <label class="cursor-pointer label">\n          <span class="label-text">我的工作台</span> \n          <input type="checkbox" id="my_page_config" class="toggle toggle-primary" />\n        </label>\n        <label class="cursor-pointer label">\n          <span class="label-text">问题列表</span> \n          <input type="checkbox" id="issues_config" class="toggle toggle-primary" />\n        </label>\n        <label class="cursor-pointer label">\n          <span class="label-text">成员列表</span> \n          <input type="checkbox" id="member_list_config" class="toggle toggle-primary" />\n        </label>\n        <label class="cursor-pointer label">\n          <span class="label-text">彩蛋开关</span> \n          <input type="checkbox" id="eggshell_config" class="toggle toggle-primary" />\n        </label>\n      </div>\n      </swal-html>\n    ', t.append(n, i);
        }
    }(), setInterval((() => o()), 6e4);
}

function o() {
    n({
        method: "GET", url: "http://redmine-pa.mxnavi.com/cardinfos", onload: e => {
            var n, i;
            const s = (new DOMParser).parseFromString(e.response, "text/html"),
                r = Array.from(s.querySelectorAll("#workreport-table tr td")), o = function (e, n) {
                    if (e && n) {
                        const i = t().get("hours") >= 13, s = `<span>今日已工作<span class="blink-text">${e}</span>`,
                            r = t(n);
                        let o = t().diff(r, "second") - 3600 * Number(e);
                        i && (o -= 3600);
                        const l = `<span style="padding-left:20px;display:inline-block;">预计下班时间 <span class="blink-text">${r.add(9, "hours").add(o, "second").format("HH:mm:ss")}</span></span>`;
                        let a = "";
                        return Number(e) > 8 && (a = `<span style="padding-left:20px;display:inline-block;">今日已加班 <span class="blink-text">${(Number(e) - 8).toFixed(2)}</span>小时</span>`), s + l + a
                    }
                    return ""
                }(null == (n = r[r.length - 1].textContent) ? void 0 : n.trim(), null == (i = r[1].textContent) ? void 0 : i.trim());
            o && function (t) {
                var e;
                let n = document.querySelector("#rikka-workTime");
                n ? n.innerHTML = t : (n = document.createElement("li"), n.id = "rikka-workTime", n.innerHTML = t, n.style.marginLeft = "100px", null == (e = document.querySelector("#main-menu ul")) || e.append(n));
            }(o);
        }
    });
}

function p() {
    n({
        method: "GET", url: "http://redmine-pa.mxnavi.com/cardinfos", onload: e => {
            var n, i;
            const s = (new DOMParser).parseFromString(e.response, "text/html"),
                r = Array.from(s.querySelectorAll("#workreport-table tr td")), o = function (e, n) {
                    if (e && n) {
                        const i = t().get("hours") >= 13, s = `<span>今日已工作<span class="blink-text">${e}</span>`,
                            r = t(n);
                        let o = t().diff(r, "second") - 3600 * Number(e);
                        i && (o -= 3600);
                        const l = `<span style="padding-left:20px;display:inline-block;">预计下班时间 <span class="blink-text">${r.add(9, "hours").add(o, "second").format("HH:mm:ss")}</span></span>`;
                        let a = "";
                        return Number(e) > 8 && (a = `<span style="padding-left:20px;display:inline-block;">今日已加班 <span class="blink-text">${(Number(e) - 8).toFixed(2)}</span>小时</span>`), s + l + a
                    }
                    return ""
                }(null == (n = r[r.length - 1].textContent) ? void 0 : n.trim(), null == (i = r[1].textContent) ? void 0 : i.trim());
            o && function (t) {
                var e;
                let n = document.querySelector("#rikka-workTime");
                n ? n.innerHTML = t : (n = document.createElement("li"), n.id = "rikka-workTime", n.innerHTML = t, n.style.marginLeft = "100px", null == (e = document.querySelector("#main-menu ul")) || e.append(n));
            }(o);
        }
    });
}

function l(t) {
    const e = document.querySelector(`#${t}`);
    if (e) {
        const n = s(t);
        e.checked = n, e.addEventListener("change", (e => {
            localStorage.setItem(`enhance_${t}`, JSON.stringify(e.target.checked));
        }));
    }
}

function a() {
    const t = document.createElement("tr");
    return t.className = "issue tracker-6 status-1 priority-4 priority-default behind-schedule assigned-to-me gradient-bg-009 my-page-tr", t.innerHTML = '\n    <td class="checkbox hide-when-print"><input type="checkbox" name="ids[]" value="88888"></td>\n    <td class="id"><a >88888</a></td>\n    <td class="project"><a >CP422001.广汽传祺_IM</a></td>\n    <td class="tracker">Bug-ST</td>\n    <td class="status">新</td>\n    <td class="subject"><a>【传祺IM】正式环境，服务器开小差了</a></td>\n    <td class="buttons"><a title="行为" class="icon-only icon-actions js-contextmenu" href="#">行为</a></td>\n  ', t.querySelectorAll("a").forEach((t => {
        t.addEventListener("click", (() => {
            e.fire({icon: "error", title: "温馨提示", html: "具体bug请联系赵姐", showConfirmButton: !1});
        }));
    })), t
}

function c() {
    if ("xxxxx" === i()) {
        const t = document.querySelector(".list.issues tbody");
        null == t || t.append(a()), null == t || t.append(a());
    }
    const t = document.querySelectorAll(".list.issues tbody tr");
    t.length && Array.from(t).filter((t => {
        var e, n;
        return null == (n = null == (e = t.querySelector(".tracker")) ? void 0 : e.textContent) ? void 0 : n.toLowerCase().includes("bug")
    })).some((t => {
        t.classList.add(`gradient-bg-${(31 * Math.random()).toFixed(0).padStart(3, "0")}`), t.classList.add("my-page-tr"), Array.from(t.querySelectorAll("td")).some((t => {
            t.classList.add("highlight-text");
        })), Array.from(t.querySelectorAll("a")).some((t => {
            t.classList.add("highlight-text");
        }));
    }));
}

function d(t) {
    t.preventDefault();
    const n = function (t) {
        const e = {};
        let n = "";
        return t.filter((t => 13 === t.childElementCount || 10 === t.childElementCount)).some((t => {
            var i, s;
            let r = 6;
            10 === t.childElementCount && (r = 5);
            const o = Number(null == (i = t.children[r].textContent) ? void 0 : i.trim());
            13 === t.childElementCount ? (n = (null == (s = t.children[0].textContent) ? void 0 : s.trim()) ?? "", e[n] = o) : e[n] += o;
        })), Object.keys(e).map((t => ({date: t, hours: Number(e[t].toFixed(2))})))
    }(Array.from(document.querySelectorAll("#workreport-table tbody tr"))), i = function (t) {
        return t.map((t => {
            const e = new Date(t.date), n = e.getDay(),
                i = HolidayUtil.getHoliday(e.getFullYear(), e.getMonth() + 1, e.getDate());
            let s = Number(t.hours) - 8;
            return i ? s = i.isWork() ? s : Number(t.hours) : 0 !== n && 6 !== n || (s = Number(t.hours)), {
                date: t.date,
                overtimeHours: s
            }
        })).filter((t => t.overtimeHours > 0))
    }(n);
    !function (t) {
        const n = t.map((t => `${t.date} 加班${t.overtimeHours.toFixed(2)}小时`)),
            i = t.reduce(((t, e) => t + e.overtimeHours), 0).toFixed(2);
        console.log(`本月共加班 %c${i}`, "color:red", "小时"), n.push(`本月共加班${i}小时`), n.push(`本月共加班${i}小时`), e.fire({
            icon: "success",
            title: "加班统计",
            html: n.map((t => `<p class="alert-p">${t}</p>`)).join(""),
            showConfirmButton: !1
        });
    }(i);
}

function u() {
    var t;
    const e = function (t, e) {
            const n = document.createElement("input");
            return n.type = "button", n.value = t, n.style.marginLeft = "4px", n.addEventListener("click", e), n
        }("加班统计", d),
        n = null == (t = document.querySelector(".from-table input[name='commit']")) ? void 0 : t.parentNode;
    n && (n.style.display = "flex", n.style.justifyContent = "center", n.appendChild(e));
}

function h(t) {
    return t.some((t => location.href.startsWith(t)))
}

function p(t) {
    return null !== location.href.match(t)
}
