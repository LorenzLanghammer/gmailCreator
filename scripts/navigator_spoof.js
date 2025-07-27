(() => {{
    const navigatorProto = Navigator.prototype;

    Object.defineProperty(navigatorProto, 'hardwareConcurrency', {{
        get: () => {hc},
        configurable: true
    }});

    Object.defineProperty(navigatorProto, 'deviceMemory', {{
        get: () => {dm},
        configurable: true
    }});

}})();
