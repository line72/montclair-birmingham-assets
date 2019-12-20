# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'birmingham',
    package_name = 'montclair-birmingham',
    name = 'Birmingham Transit',
    description = 'Real Time Bus Tracking for Birmingham, AL',
    url = 'https://montclair.line72.net',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.2.1',
        revision = 3,
        title = 'Birmingham Transit',
        first_run_text = "Welcome to Birmingham, AL's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '1.0.0-3',
        revision = 1,
        app_id = 'net.line72.montclair',
        app_store_id = 'id1418953482',
        app_store_url = 'https://itunes.apple.com/us/app/montclair/id1418953482'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.0-2',
        revision = 1,
        app_id = 'net.line72.montclair',
        play_store_url = 'https://play.google.com/store/apps/details?id=net.line72.montclair'
    )
)
