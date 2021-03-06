# Open-Elevation (forked)

[https://open-elevation.com](https://open-elevation.com)

A free and open-source elevation API.

**Open-Elevation** is a free and open-source alternative to the [Google Elevation API](https://developers.google.com/maps/documentation/elevation/start) and similar offerings.

This service came out of the need to have a hosted, easy to use and easy to setup elevation API. While there are some alternatives out there, none of them work out of the box, and seem to point to dead datasets. **Open-Elevation** is [easy to setup](https://github.com/cl00e9ment/open-elevation/blob/master/docs/host-your-own.md), has its own docker image and provides scripts for you to easily acquire whatever datasets you want. We offer you the whole world with our [public API](https://github.com/cl00e9ment/open-elevation/blob/master/docs/api.md).

If you enjoy our service, please consider [donating to us](https://open-elevation.com#donate). Servers aren't free :)

**API Docs are [available here](https://github.com/cl00e9ment/open-elevation/blob/master/docs/api.md)**

You can learn more about the project, including its **free public API** in [the website](https://open-elevation.com)

## What's different from the [official image](https://hub.docker.com/r/openelevation/open-elevation)?

- The dataset URLs has been updated.
- You can restrict the access to the API using keys.
- An arm64 image is available, so you can run the server on a Raspberry Pi for example.
