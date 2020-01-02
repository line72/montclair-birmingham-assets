# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'birmingham',
    package_name = 'montclair-birmingham',
    name = 'Go Birmingham',
    description = 'Real Time Tracking of the Buses for Birmingham, AL',
    url = 'https://birmingham.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.2.2',
        revision = 1,
        title = 'Go Birmingham',
        first_run_text = "Welcome to Birmingham, AL's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.birmingham',
        app_store_id = '',
        app_store_url = 'REPLACE_ME'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.birmingham',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.birmingham'
    )
)
