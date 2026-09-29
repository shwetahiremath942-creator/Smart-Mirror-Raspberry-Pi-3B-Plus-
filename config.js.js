let config = {
    address: "localhost",
    port: 8080,
    basePath: "/",
    ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"],
    language: "en",
    timeFormat: 12,
    units: "metric",

    modules: [
        {
            module: "alert",
        },
        {
            module: "clock",
            position: "top_left"
        },
        {
            module: "calendar",
            header: "Upcoming Events",
            position: "top_left",
            config: {
                calendars: [
                    {
                        symbol: "calendar-check",
                        url: "webcal://www.calendarlabs.com/ical-calendar/ics/76/US_Holidays.ics"
                    }
                ]
            }
        },
        {
            module: "currentweather",
            position: "top_right",
            config: {
                location: "Bengaluru",
                locationID: "1277333", // OpenWeatherMap City ID
                appid: "YOUR_OPENWEATHER_API_KEY"
            }
        },
        {
            module: "newsfeed",
            position: "bottom_bar",
            config: {
                feeds: [
                    {
                        title: "National News",
                        url: "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
                    }
                ],
                showSourceTitle: true,
                showPublishDate: true
            }
        }
    ]
};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") { module.exports = config; }