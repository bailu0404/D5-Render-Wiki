# How to use City Generator?

The entry of City Generator feature is integrated in the drop-down menu of the ‘Terrain’ button in the navigation bar. It supports two ways to fetch city data information.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F2VC1NHyjQM5EVa4pQFCS%252Fimage.png%3Falt%3Dmedia%26token%3D639feb1a-9cdc-471c-9e08-f847fb28a408&width=768&dpr=3&quality=100&sign=5c22fe36&sv=2)

## 1. D5 Render 3.0-City Feature Overview

The city module in D5 Render 3.0 is designed to quickly and efficiently generate buildings and roads around your site, helping you plot swiftly during the analysis and effect drawing stages of the project. This includes two main modes: White mode and Architectural Style mode.

White ModeArchitectural Style Mode![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FuWu73fraDolZkqtxL8mS%252Fimage.png%3Falt%3Dmedia%26token%3Dd008f9ff-ccf1-4c5e-8ca1-4b33bc5a01c6&width=768&dpr=3&quality=100&sign=6dfa8bdc&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FOmqnUZDoO4ZzWfrUP1Ok%252Fimage.png%3Falt%3Dmedia%26token%3Da3356955-5e8d-459e-970d-42147dd40605&width=768&dpr=3&quality=100&sign=2fe0e5bc&sv=2)

- Whether it is in the white model mode or architectural style mode, we support the following operations.

  - ****Proportional adjustment**** of the overall height of the building group
  - Adjustment of individual building height
  - ****Proportional adjustment**** of the overall width of the road group
  - Adjustment of single road width
- In the white model mode, we also support the following operations.

  - Adjustment of the overall color, map, and opacity of the building group
  - Adjustments to the overall color, map, and opacity of the road Group
- In the architectural style mode, we have three preset styles: ****General, European,**** and ****Transparent Block.**** To ensure your customization requirements are met, we have set adjustable parameters for building groups and individual buildings.

  - In General and European style

    - For the building group, you can randomly generate a new map for the whole building group by adjusting the random map. The Random Texture option enables the generation of new textures for the entire building group. Additionally, the commercial slider adjusts the degree of modernity of the external facades.
    - For a single building, you can adjust the elevation map and roof style of that building, and you can copy the elevation map you like to another building.
  - In Transparent Block Style

    - For building groups, you can adjust the color and opacity of transparent blocks.
    - For a single building, you can adjust the first floor height and the standard floor height to control the vertical positioning of floors within the transparent block.

---

## 2. D5 Render 3.0-Detailed Description of City Feature

### 2.1 Select the city area you want to generate

#### 2.1.1 Select the city area you want to generate in two ways.

> ℹ️ > You can enlarge the window by dragging the right and lower sides of the window. In subsequent updates, we will also support the dragging method to enlarge the window.

Use default map controlsUse your own shp file![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F26Gc3hhLhK9ZTXiSxPcA%252Fimage.png%3Falt%3Dmedia%26token%3Dc0ce3922-9528-4f81-8f66-1e0d2c82789c&width=768&dpr=3&quality=100&sign=8e3f44d7&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FnxIeY49Q332Xid93vpsg%252Fimage.png%3Falt%3Dmedia%26token%3D70718305-7aa6-4a84-9b79-e23a710aab38&width=768&dpr=3&quality=100&sign=d37fcd1c&sv=2)

#### 2.1.2 Enter a city name to lock the city area you want to generate.

Using the following image as an example, we will provide locations based on the name you entered. ****Click the location in the drop-down menu**** to jump to this area.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FFQfkLmFJK9eydFGOMcMj%252Fimage.png%3Falt%3Dmedia%26token%3D9b691a50-99e6-4432-9b97-59986514561e&width=768&dpr=3&quality=100&sign=4574043c&sv=2)

#### 2.1.3 Select the generated content of the selection area.

By default, building, road, greenery, and water will be downloaded. To include satellite maps, please select the satellite option.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fbfq8AUzJ4VSUNelbEz7i%252Fimage.png%3Falt%3Dmedia%26token%3D2136397c-04c2-4348-abbd-6221868745bb&width=768&dpr=3&quality=100&sign=5c533cf7&sv=2)

#### 2.1.4 Generation Time

The generation speed depends on the size of the selected area. For example, processing a 4 km by 4 km area typically requires up to five minutes. Please wait patiently.

### 2.2 City Level

The imported cities are organized into three hierarchical levels: City, Buildings/Roads/Greenery/Water/Satellite/Ground, and individual buildings or roads. Each level allows for the adjustment of specific parameters. The following sections provide a detailed introduction to the two modes: the white model mode and architectural style mode.

CityBuildings/RoadsIndividual building/road

- By default, the city import selects the entire city.
- To select the entire city, click on the city name in the left sidebar.

- Click on any building to select the entire building group.
- Click on any road to select the entire road group.
- You can also select building and road groups by clicking on the left sidebar.

- Double-click a building to select it individually.
- Double-click a road to select it individually.
- You can also select individual buildings or roads from the left sidebar.
![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F8ohYF0BTbKXiZk7huXez%252Fimage.png%3Falt%3Dmedia%26token%3Dd01e49a0-71e1-44f5-be92-82f52e2ad0ac&width=768&dpr=3&quality=100&sign=4757d6b6&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FTVsQjVRUXMNPL2f5hEER%252Fimage.png%3Falt%3Dmedia%26token%3Dd6c7cbdf-96b1-4a8e-a20a-9e9991446583&width=768&dpr=3&quality=100&sign=49c14464&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FqCxadVcLycN9kJ3wBYZG%252Fimage.png%3Falt%3Dmedia%26token%3Dd766683a-5fa5-4b20-8a12-fe8531186be8&width=768&dpr=3&quality=100&sign=a6babc4c&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fk9M0vLZuwYu4TsZTtxTD%252Fimage.png%3Falt%3Dmedia%26token%3D3568d0f9-e1a5-44a4-a5f4-8d077130cbe5&width=768&dpr=3&quality=100&sign=637f02f1&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FzvjVVKxmoYtfWkmqdcN2%252Fimage.png%3Falt%3Dmedia%26token%3Dda616c9f-7d54-428e-abed-0e6551dd0326&width=768&dpr=3&quality=100&sign=1dd6bcbd&sv=2)

### 2.3 White Model Mode

> ⚠️ > Note: When you select the entire building group, the height value in the right-hand sidebar is a proportional value. For example, if you set it to 50, the height of all buildings in the group will become 50% of their default height. The same applies to roads.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FZM5Hi3KKJVjb2VNBmtGt%252Fimage.png%3Falt%3Dmedia%26token%3Dd573bc9c-baab-410b-9f14-37ca0d1080f8&width=768&dpr=3&quality=100&sign=44cdd74e&sv=2)

#### 2.3.1 Switch Between White Model Mode and Architectural Style Mode

The ****Style**** switch in the right sidebar can be activated when a building group is selected to apply style materials to the entire group. Alternatively, style materials can be assigned to individual buildings when a single building is selected.

Apply materials to the building group as a wholeApply materials to a single building![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FEDYFncHVkKWEKi25XPAC%252Fimage.png%3Falt%3Dmedia%26token%3De5145bd2-9b5e-4f5e-96ea-556d1f213b00&width=768&dpr=3&quality=100&sign=d59ca213&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Feb5hlpN8o6KmTLLxet7J%252Fimage.png%3Falt%3Dmedia%26token%3Dc946d4db-8930-45e5-8485-ca4acff80a7a&width=768&dpr=3&quality=100&sign=60530d84&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fp6qFV8DmMgxtwG2jhKEP%252Fimage.png%3Falt%3Dmedia%26token%3D9dcbb78d-1656-4856-bc27-f99772bd9c87&width=768&dpr=3&quality=100&sign=7eb5f2c7&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FLLzSZpBk11HtTi2weAK4%252Fimage.png%3Falt%3Dmedia%26token%3D43b95a9c-d1ab-4ce9-abcc-9bb2c6e49ae1&width=768&dpr=3&quality=100&sign=7373c726&sv=2)

### 2.4 Architectural Style Mode

#### 2.4.1 Select the button located at the edge of the style list for additional adjustable parameters.

When you select an entire building group, you can apply random textures to change the texture style throughout the city on a large scale.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FBo7UpAuvhjIVdaHqSucf%252Fimage.png%3Falt%3Dmedia%26token%3D9bf817a0-fe28-40f7-b7ee-d21e38b9a880&width=768&dpr=3&quality=100&sign=f9d3d5bd&sv=2)

#### 2.4.2 Control of individual architectural styles

When you select an individual building, you retain control over its style.

> ⚠️ > Note: All buildings with office properties will not change significantly when switching between General and European.

GeneralEuropeanTransparent Block![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7n83KFF1lU6R32Mgq5rD%252Fimage.png%3Falt%3Dmedia%26token%3D451bac90-df9b-4100-8ea7-73395b56dc7e&width=768&dpr=3&quality=100&sign=e1b7e7c7&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F9kZ5jZM2LqknXRE5aFS1%252Fimage.png%3Falt%3Dmedia%26token%3D67f45c3c-2695-4974-ba0d-571283fc9813&width=768&dpr=3&quality=100&sign=e6bf7719&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FCvFcj8M7mDCBtMO5JriN%252Fimage.png%3Falt%3Dmedia%26token%3Dbc387690-c083-40fa-b736-429b6bd3f5c5&width=768&dpr=3&quality=100&sign=7b620b34&sv=2)

#### 2.4.3 Adjustment to the material of individual building facades

You can adjust the building facade both ****randomly**** and by ****adjusting the current building properties****.

RandomAdjust the current building properties![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F2vrzWvHM9TxmbYD7jeL5%252Fimage.png%3Falt%3Dmedia%26token%3D4760c552-efff-4a1a-a6c4-8953978c550f&width=768&dpr=3&quality=100&sign=76af26cc&sv=2)

Random Style 1

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fv31duIh7FbnksjiXkV4x%252Fimage.png%3Falt%3Dmedia%26token%3D8a267400-6179-4c3f-bdf7-80d8d8b7ad79&width=768&dpr=3&quality=100&sign=f3535831&sv=2)

Residential

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FjdjjaKRRgRMYZgoP4G0o%252Fimage.png%3Falt%3Dmedia%26token%3D13e644c5-f8f0-45db-8b9e-e271313f26c7&width=768&dpr=3&quality=100&sign=bd2ece0b&sv=2)

Random Style 2

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F1Tc2sD5JKLWKBfegv4YA%252Fimage.png%3Falt%3Dmedia%26token%3D8f15845a-307e-4b8d-89b1-6d6777bb095f&width=768&dpr=3&quality=100&sign=ff61d86d&sv=2)

Residential

You can copy the material of the current building to another building.

Before copyingAfter copying![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FN2Iy7gdw1etT26O642Xp%252Fimage.png%3Falt%3Dmedia%26token%3Da5457b84-c069-4645-b6b6-1db910d1bdbf&width=768&dpr=3&quality=100&sign=cbc69455&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FiQJWi6sEBnBrbdMNDUs8%252Fimage.png%3Falt%3Dmedia%26token%3D3e9c6835-4bb7-4076-a65a-7683105bcd18&width=768&dpr=3&quality=100&sign=806dc402&sv=2)

#### 2.4.4 Adjustments to the roof material of individual buildings

Click this button in the image below to adjust the roof style of the building

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FQuRdXt0zt7IMgMSFL1va%252Fimage.png%3Falt%3Dmedia%26token%3D51bd2c93-a86e-48d9-bb05-994cb3642ab2&width=768&dpr=3&quality=100&sign=373d3dc4&sv=2)

We provide you with three default roof styles, namely: flat roof, green roof and stairwell. Take the building below as an example to see the effect of different styles.

> ⚠️ > Please note the two points below:

1. If the roof generated by default is already a stairwell roof, selecting the stairwell option again will not alter the visual display in any way. The same applies to flat roofs.

2. Whenever you depart from the default roof and select any of the aforementioned roof types, the flat roof option will be automatically selected.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FU8Z1s8ZX20yGnDgA7I8i%252Fimage.png%3Falt%3Dmedia%26token%3D92f293ba-80b1-43cf-a833-4817cf00d9b3&width=768&dpr=3&quality=100&sign=f06cb9f1&sv=2)Flat RoofGreen RoofRoof with StairwellMix![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fqo6PwbxzEVp8QRJrdsMs%252Fimage.png%3Falt%3Dmedia%26token%3D0f6aafc6-5125-4ac0-82a0-73c9c9eff16e&width=768&dpr=3&quality=100&sign=a9129ddc&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F7FbsxQp0u8hyZMg9xJnz%252Fimage.png%3Falt%3Dmedia%26token%3De5a98c5c-1e66-4da7-9ae0-9b95de3f47b5&width=768&dpr=3&quality=100&sign=15f573f7&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fq0m8zEP1UpBgubmSTxBj%252Fimage.png%3Falt%3Dmedia%26token%3D346c9129-00cc-4d5d-8cf1-202f29b16e9f&width=768&dpr=3&quality=100&sign=3c97a0bb&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FhVRSfQkNUhuTkjrrk7iO%252Fimage.png%3Falt%3Dmedia%26token%3Df6150524-8767-479a-9abd-d4794f6aad0e&width=768&dpr=3&quality=100&sign=519dd02b&sv=2)

---

## City Feature Guide I

### OSM Integration

Integrates the open source data from OpenStreetMap to automatically analyze and generate roads, buildings, terrain, and other topography features, enabling effortless site context creation.

> **Note:**
>
> **\*OSM (OpenStreetMap) file is a map data file based on the OpenStreetMap data. These files contain the topography information of roads, buildings, terrain, etc., and are widely used in map drawing and urban planning.**

#### 1. OSM import

- Click Terrain-City, then zoom in and out in the pop-up window to the desired range using the '+' & '-' controls or the mouse wheel.
- Supports quick location of the target area by entering its name or moving the selection box. The area is restricted to ****4km\*4km****.
- Supports filtering and importing certain topography features such as buildings, roads, greenland, water, or satellite images.

> ⚠️ > ****Note:****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FumQ9DeesM3X2v2d5Kjsc%252Fosm%2520%281%29.gif%3Falt%3Dmedia%26token%3Dd450e232-f436-4d3b-96a1-01b1eaa87d25&width=768&dpr=3&quality=100&sign=890c7928&sv=2)

#### 2. Parameter Editing

After the import is complete, the map model will appear in the viewport, with its topography elements as a group within the object list.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FkzCpWLL2rmfKr1eDQvS8%252Fimage.png%3Falt%3Dmedia%26token%3Ddd0209c0-e8d8-4923-9b45-1dd42beda236&width=768&dpr=3&quality=100&sign=5d355ce0&sv=2)

****Building Group Settings****

- Elevation (based on original heights)&Random elevation
- Base color&Base color map
- Opacity option
- UV parameters(including Triplanar and UV Randomizer)
- (Single building within group) Height

****Road Group Settings****

- Width
- Base color&Base color map
- UV parameters(including Triplanar and UV Randomizer)

****Water, Greenland Groups****

- Base color&Base color map
- UV parameters(including Triplanar and UV Randomizer)

****Satellite, Ground Groups****

- Base color&Base color map

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FTmpvZ3S830lASCWneDgg%252F%25E5%258F%2582%25E6%2595%25B05.gif%3Falt%3Dmedia%26token%3D55fdce17-ec19-47ba-a2f6-46a0971273ad&width=768&dpr=3&quality=100&sign=a5805e47&sv=2)

#### 3. Delete/replace City group

- Right-click it from the object list to delete the whole city group
- Select the city group from the object list, and click 'Reselect' icon in the right sidebar. Select area in the pop-up window to ****recreate****.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fc7Ui3Fa0VN6coSvV6YpK%252Fimage.png%3Falt%3Dmedia%26token%3D46529fac-4a10-44fa-882f-dda82fa29b16&width=768&dpr=3&quality=100&sign=4d1a5f40&sv=2)

### Shapefile(.shp) Import

Supports Shapefile import for effortless site context creation.

> **\*.shp file is ESRI Shapefile data format widely used in geographic information systems (GIS). It typically contains vector data, such as points, lines, and polygons to represent geographic features including buildings, roads, rivers, and administrative divisions.**

#### 1. .Shp Import

- Click Terrain-City, and import .shp file in the pop-up window. Supports multi-selection and uploading single file up to ****10 MB****. If the size is exceeded, a pop-up error will be reported.
- D5 automatically analyzes the geographic information in the .shp file and generates corresponding 3D models.
- Each imported file is stored as a group in the object list, containing three types of objects: "Buildings," "Roads," and "Undefined." Supports repositioning or rotating the entire group.

> ⚠️ > ****Note:****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FpGJSnATo76UVE7vTRD7V%252Fimage.png%3Falt%3Dmedia%26token%3Df8d3729d-ac6f-4694-a80a-fc232d9687bd&width=768&dpr=3&quality=100&sign=61b1e421&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F1GUDLwMwmu2A2nThmI9Z%252Fshape.gif%3Falt%3Dmedia%26token%3D22ce9133-5efa-45d2-9edd-e72cda34278d&width=768&dpr=3&quality=100&sign=e0e940dd&sv=2)

#### 2. Parameter Editing

****Building and Undefined Group:****

- Elevation (based on original heights)&Random elevation
- Base color&Base color map
- Opacity option
- UV parameters(including Triplanar and UV Randomizer)
- (Single building within group) Height

****Road Group:****

- Width
- Base color&Base color map
- UV parameters(including Triplanar and UV Randomizer)

> ℹ️ > ****FAQs****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FFaeoD38S7OCsUP5OPP6L%252Fimage.png%3Falt%3Dmedia%26token%3D3f2a6b66-4ff7-4242-9165-5c8511625a7a&width=300&dpr=3&quality=100&sign=68f34971&sv=2)

- ****Unsupported data type:**** D5 currently supports polygon and polyline data. Other data formats might fail to be analyzed.

- ****Shapefile content:**** Ensure that all related files (such as .shx and .dbf) are complete and placed in the same directory.

- ****Read&Write permissions:**** Ensure that the current Windows account has permissions to access, read, and write the current Shapefile file and its related files, especially if the file is stored on a network drive or shared folder.