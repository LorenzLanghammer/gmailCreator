(() => {{
            const spoofedTimeZone = {spoofed_timezone};
            const originalResolvedOptions = Intl.DateTimeFormat.prototype.resolvedOptions;
            Intl.DateTimeFormat.prototype.resolvedOptions = function() {{
                const options = originalResolvedOptions.apply(this, arguments);
                options.timeZone = spoofedTimeZone;
                return options;
            }};

            const originalGetTimezoneOffset = Date.prototype.getTimezoneOffset;
            Date.prototype.getTimezoneOffset = function() {{
                return {spoofed_offset_minutes};
            }};

            const offsetMs = {spoofed_offset_minutes} * 60 * 1000;
            const OriginalDate = Date;
            function FakeDate(...args) {{
                if (args.length === 0) {{
                    return new OriginalDate(OriginalDate.now() - offsetMs);
                }}
                return new OriginalDate(...args);
            }}
            FakeDate.UTC = OriginalDate.UTC;
            FakeDate.now = () => OriginalDate.now() - offsetMs;
            FakeDate.parse = OriginalDate.parse;
            FakeDate.prototype = OriginalDate.prototype;
            window.Date = FakeDate;
        }})()



        