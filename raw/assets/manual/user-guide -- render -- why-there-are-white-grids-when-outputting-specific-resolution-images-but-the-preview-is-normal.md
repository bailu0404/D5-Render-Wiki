# Why there are white grids when outputting specific resolution images, but the preview is normal?

If you have ****semi-transparent curtains/custom blinds**** in your scene, some of the scenes may have white grids in the ↓ image when outputting at certain resolutions (the preview is normal).

This is a known issue with the current version and can be fixed by adjusting the material of the curtain/blinds model to 100% opacity (adjusting the material to a transparent material template & opacity parameter to 100%), then you can get the normal output effect. We will fix it in subsequent releases.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FeAciUPLeOiq2SfVflVt0%252Fimage.png%3Falt%3Dmedia%26token%3Dbddf0b2e-5cee-4cea-a2e7-a1cda6cea563&width=768&dpr=3&quality=100&sign=3df0c54&sv=2)

there are white grids when outputting specific resolution images (the preview is normal)