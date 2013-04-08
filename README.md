anode
=====

A Python flask [boomerang](https://github.com/yahoo/boomerang) beacon endpoint with graphs!

These graphs will show you the total ammount of time that users had to wait for your page to load.

![anode](https://f.cloud.github.com/assets/30399/294818/77216166-9418-11e2-9618-3c3d35de59bd.png)

Make sure to install the requirements from requirements.txt

Then you need to make sure that all the pages you want to phone home have this JavaScript

The `beacon_url` needs to be the address of the Flask server

```JavaScript
  <script src="https://raw.github.com/yahoo/boomerang/master/boomerang.js" type="text/javascript"></script>
  <script>
    tplPrefix = 'ds_';
    // configure boomerang
    BOOMR.init({
      beacon_url: '{{ base_js_extra }}',
      site_domain: window.location.host,
      BW: {
        base_url : 'https://raw.github.com/yahoo/boomerang/master/images/',
        nruns: 3
      }
    });
    // start the timer
    BOOMR.plugins.RT.startTimer( tplPrefix + 'head');
  </script>
```

This is GPL code, this is also not ready for other people to use it.
