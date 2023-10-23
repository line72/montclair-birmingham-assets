/* -*- Mode: rjsx -*- */

/*******************************************
 * Copyright (2018)
 *  Marcus Dillavou <line72@line72.net>
 *  http://line72.net
 *
 * Montclair:
 *  https://github.com/line72/montclair
 *  https://montclair.line72.net
 *
 * Licensed Under the GPLv3
 *******************************************/

import AvailtecParser from './AvailtecParser';

class Configuration {
    constructor() {
        // Birmingham, AL
        this.center = [33.5084801, -86.8006611];
        this.tileserver = {
            url: 'https://birmingham.gotransitapp.com/tiles/{z}/{x}/{y}.png',
            subdomains: ''
        };

        this.agencies = [
            {
                name: 'Routes',
                parser: new AvailtecParser('https://birmingham.gotransitapp.com/api/no.php/InfoPoint')
            }
        ];
    }
}

export default Configuration;
