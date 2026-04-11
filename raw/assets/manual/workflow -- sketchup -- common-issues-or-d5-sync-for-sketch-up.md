# Common issues | D5 Sync for Sketch up

## 1. Why doesn't the model appear in the D5 render after clicking the D5 Converter - SketchUp sync button? There are two possible reasons:

## 2. Why doesn't the D5 converter - SketchUp show in the toolbar of SketchUp after installation?

Reference: rbz installation method

## 3. Why the D5 converter - SketchUp indicates "load error su\_to\_d5render"?

Since the SketchUp installer used is missing the D5 Converter runtime dependency profile, it is recommended to reinstall SketchUp using an installer from another source, and then reinstall D5 Converter - SketchUp.

## 4. D5 Converter - SketchUp indicates "Please install the latest version of D5 Render, if you have already installed the latest version, please manually select the installation path".

## 5. Why the lights become solid model after importing .skp file into D5 render?

****Solution:**** Open this skp file in SketchUp, hide all the light source by D5 Converter - SketchUp with one click, save the skp file, and then import it into D5 render directly.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FuOg09pX6skb451g9CDPs%252Fimage.png%3Falt%3Dmedia%26token%3De6bd438d-9341-4da9-be9e-d7fdc5382be9&width=768&dpr=3&quality=100&sign=7ba33de8&sv=2)

### The light source tool of D5 Converter - SketchUp is only applicable to the workflow of plugin synchronization.

Under the direct read workflow, the D5 light source added through the plugin will become an entity model and the light source be read directly. Under the workflow of plugin synchronization, the D5 light source added in SketchUp is hidden by default, and the light source is displayed in the scene of the D5 Render.

## 6. Why are some models not displayed when imported into D5 directly or linked through the D5 Converter - SketchUp?

****Solution:**** Explode and scale define the model in SketchUp, then import or link to D5.