# How to use Cesium?

> ⚠️ > ****Note:****

- ****Professional**** users need to use D5 Render client version 3.0 or above to use Cesium function. Team users are not affected.
- Users with ****Community**** versions and ****Education**** licences are currently unable to use Cesium.

## Cesium Service Integration

## 1. Function Introduction

Cesium is an open 3D geospatial platform with massive global terrain, 3D architecture and image data.

D5 Render integrates Cesium services to allow users to load real geographic information data (such as city models, Terrain elevations, satellite images) directly into D5 scenes. This provides a real "Digital Foundation" for your design, which is very suitable for urban planning, landscape design, traffic simulation and other projects that need to be integrated with the surrounding real environment.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FCIbDrGf5e27SQwJ80Tq4%252Fimage.png%3Falt%3Dmedia%26token%3D8e6e70d7-4241-4bee-a773-d9380c6e9d4a&width=768&dpr=3&quality=100&sign=a310e1b3&sv=2)

#### Core features and considerations

Before using cesium in D5, please understand how it works:

- ****Cloud data streaming:**** Cesium data needs to be used online throughout the process. D5 only reads the data stream and does not save the large GIS data download to your local archive.
- ****Real-time and caching:**** Because the data is not stored locally, it needs to be reloaded from the server every time the project is opened. As a result, the terrain and buildings may take a short time to refresh.
- ****Layer overlay logic:**** Cesium data is composed of multiple "layers" (for example: a layer of satellite image + a layer of terrain + a layer of 3D buildings). In D5, these data are superimposed using the same coordinate system and together constitute the background environment.

## 2. Preparation: Obtain Cesium Authorization

Whether it is an individual user or a team user, you first need to have a Cesium account and obtain an Access Token (Access Token).

a. You can upload your own mapping data (users in Mainland China are not permitted to upload data).

b. You can also add the official free global base data from the `Asset Depot`.

> ⚠️ > Note: To use these assets for commercial purposes, be sure to check the official Cesium authorization subscription instructions.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fn9jEoBgVYFLJ7j67ZP8z%252Fimage.png%3Falt%3Dmedia%26token%3Db436437a-91af-441f-ad57-7778c6bd1be3&width=768&dpr=3&quality=100&sign=446490f7&sv=2)

You can manage geographic information data assets on the Cesium ion platform.

a. Enter`Access Tokens`page.

b. Click`Create token`to create a new token (you cannot use the `Default`token, because it does not have sufficient permissions)

c. Enable all the data permissions in Public scopes and the asset permissions that need to be opened.

d. Click`Create`and copy the newly generated token string.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FPKsWFUpkI1iJ9oCzOZ5X%252Fimage.png%3Falt%3Dmedia%26token%3D2c0e66ee-fef4-4d35-bd2b-8dc47566b765&width=768&dpr=3&quality=100&sign=a8c60e33&sv=2)

Create a new token and set up permissions correctly

## 3. Configure Cesium Token

> ⚠️ > Select the corresponding configuration method according to your D5 account type.

### 3.1 Individual User

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FJFoqjjk6Aiy71LPBiBmu%252Fimage.png%3Falt%3Dmedia%26token%3Dc4749cfa-a09d-41a2-a23c-98ac2c0623fa&width=768&dpr=3&quality=100&sign=5eb34805&sv=2)

Go to D5 MySpace to deploy Cesium token

### 3.2 Team User

For team users, a team administrator must log in to [D5 My Space](https://myspace.d5render.com/login) to configure the token. The configuration process is the same as for individual users. Once the setup is complete, all team members can use the Cesium feature in D5 Render client.

## 4. Using Cesium in D5 Render

### 4.1 Getting Started

Open D5 Render and click on the top menu bar `Terrain` Tools, selecting Cesium The Cesium operation panel opens.

**If you do not configure the Token, you will be prompted to go to the configuration (refer to section 3).**

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FDN0VhpgAARdt5wqBXyEr%252Fimage.png%3Falt%3Dmedia%26token%3Dfc369275-3dc7-4300-98ce-5e23e138d328&width=768&dpr=3&quality=100&sign=3f46e55&sv=2)

Open the Cesium operation panel at the top of D5 Render client

As shown in the following figure, the Cesium operation panel is mainly divided into three functional areas:

1. ****Map Preview**** This is the window for you to make a preliminary point selection.

- ****Search & Locate:**** Enter a city or landmark name in the top search bar to quickly jump to the target area.
- ****Interactive map:**** Zoom and PAN support to help you visually find the specific parcels you need to import. The center point of the map is the origin of the coordinates to be imported.

2. ****Parameter panel**** Controls the specific parameters of the imported resources precisely here:

- ****Longitude and Latitude:**** displays the precise coordinates of the center point of the current map. You can also manually enter values for fine adjustment.
- ****Scale:**** Sets the scale of the imported model in the scene.

3. ****Data Source:**** Select the map data resources you want to import into the scene.

The data sources available here depend on the resources added to My Assets in Cesium and the authorization status of the selected access token.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F6qjNrOgBfsjggc0KQ5vR%252Fimage.png%3Falt%3Dmedia%26token%3D4392847d-d1fe-4d41-b283-af26344bbb54&width=768&dpr=3&quality=100&sign=1cce27ea&sv=2)

Import geographic information data into D5 scenes via the Cesium operation panel

### 4.2 Add Cesium resources to the scene

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F6wTNlw6sFzYwPyb3H78a%252Fimage.png%3Falt%3Dmedia%26token%3Dc1ac8b69-ba73-434a-a28d-9ee3c9c7b9de&width=768&dpr=3&quality=100&sign=133ac0e4&sv=2)

The effect after importing the Cesium OSM Buildings and Google Photorealistic 3D Tiles data sources

### 4.3 Effect adjustment

After the Cesium data is loaded, you can superimpose your own design scheme onto this base to integrate it with the real‑world geographical environment. In addition, you can adjust the imported Cesium data as needed.

#### Overall adjustment

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSChGzOi0hasrPCtLHQho%252Fimage.png%3Falt%3Dmedia%26token%3D6443a67b-83a7-4549-ac14-8adc1065cbb4&width=768&dpr=3&quality=100&sign=ba4b3d9c&sv=2)

#### Detail adjustment

You can adjust some details for each data resource.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FgvLmo34s4FaU3IpSG9cf%252Fimage.png%3Falt%3Dmedia%26token%3D9f1ca5e1-c25b-449b-aeb5-ca4d39a642a3&width=768&dpr=3&quality=100&sign=6439fb6b&sv=2)

****Maximum Screen Space Error****

The smaller the value, the finer the model, but the higher the scene source consumption.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FX1CVtmeIk6YOpDh2T3yS%252Fimage.png%3Falt%3Dmedia%26token%3D9d4eef67-6183-471c-a109-fc5572977622&width=768&dpr=3&quality=100&sign=c480432&sv=2)

The effect of the Cesium OSM Buildings data source when the maximum screen error is set to 1, 5, and 50 respectively

****Range Limit****

When range restriction is turned off, all data source contents in the field of view will be displayed by default; When range restriction is turned on, only the data source contents in the entered range will be displayed.

****LOD Transition****

Controls whether the Cesium has a gradient animation when it loads data.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FsSwp7VgcLxg8O26xdcz0%252FCleanShot%25202025-12-11%2520at%252010.38.17.gif%3Falt%3Dmedia%26token%3D500aff01-d811-4083-8dab-fc858771e72f&width=768&dpr=3&quality=100&sign=17dab2d0&sv=2)

Enable LOD Transition