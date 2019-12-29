# Hosting your own Open-Elevation instance

You can freely host your own instance of Open-Elevation.

## Cloning the repository

First things first, clone the repository and `cd` onto its directory

```bash
git clone https://github.com/Cl00e9ment/open-elevation.git
cd open-elevation
```

## Getting the dataset

Open-Elevation doesn't come with any data of its own, but it offers a set of scripts to get the whole [SRTM 250m dataset](http://srtm.csi.cgiar.org/wp-content/uploads/files/250m/tiles250m.jpg).

### SRTM 250m dataset

If you wish to host the whole world, just run

```bash
docker-compose run open-elevation /code/create-dataset.sh
```

The above command should have downloaded the entire SRTM dataset and split it into multiple smaller files in the `data` directory. **Be aware that this directory may be over 20 GB in size after the process is completed!**

### Custom dataset

If you don't want to use the whole world, you can provide your own dataset in GeoTIFF format, compatible with the SRTM dataset. Simply drop the files for the regions you desire in the `data` directory. You are advised to split these files in smaller chunks so as to make Open-Elevation less memory-hungry (the largest file has to fit in memory). The `create-tiles.sh` is capable of doing this, and you can see it working in `create-dataset.sh`. Since you are using docker, you should always run the commands within the container. For example:

```bash
docker-compose run open-elevation /code/create-tiles.sh /code/data/SRTM_NE_250m.tif 10 10
```

The above example command splits `SRTM_NE_250m.tif` into 10 by 10 files inside the `/code/data` directory, which is mapped to `$(pwd)/data`.

**Do not forget to remove the original unsplited file.**

## Enabling authentication (optional)

You can enable authentication, that is to say, allow access to the API only to users that provide a key.

First thing first, turn `key_required` in `data/config.json` to `true`.

Then you can remove the `demo-key` from the `data/keys.txt` file and add others. 

## Running the Server

Now that you've got your data, you're ready to run Open-Elevation! Simply run

```bash
docker-compose up
```

You should now be able to go to `http://localhost:8080`.

To modify the port simply change the port mapping in the `docker-compose.yml` file (`ports: <the port you want here>:8080`).

## Problems

Have you found any problems? Open an issue or submit your own pull request!
