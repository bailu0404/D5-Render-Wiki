# Why does the scene made with 2.6 or previous versions look different in version 2.7?

Because we upgraded the D5 GI (global illumination) for both preview and output:

- Improved reflection algorithms with better diffuse and reflection accuracy so the real-time preview & output are closer to Ground Truth.
- Improved the accuracy of GI brightness and color from spotlights, projectors, and stage lights. The attenuation of area lights now affect GI correctly.
- Materials in video renderings can now reflect soft edges of shadows correctly.

### Interior GI Enhancements

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F0I4p0Yj1ZRJSaQ819DQH%252Fimage.png%3Falt%3Dmedia%26token%3Dcfe5a486-298a-4546-90f6-d0917d2e032a&width=768&dpr=3&quality=100&sign=26e2067b&sv=2)

2.6 GI vs 2.7 GI

### Enhanced Metal Reflections in Interior Scenes

Interior metals in 2.7 appear brighter compared to 2.6, because interior metal reflections are enhanced to get closer to Ground Truth, namely the reality.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fj3K5rorTbxZ90OmI8fk5%252F1f86c84ea6337cc38b62bcb630bf6199cce5f56d.gif%3Falt%3Dmedia%26token%3Dc29e0f44-128d-480d-b372-51b8068a3fb3&width=768&dpr=3&quality=100&sign=45b16e21&sv=2)

### Enhanced Interior Light-Dark Contrast

The GI algorithms of D5 2.7 are more accurate, resulting in enhanced contrasts between bright and dark areas. The overall shading effect is more accurate.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F2SqGX5V9KjNvtY56GYZY%252F9b5b79d18c5f28640a78da1665b88a5b06685a52.gif%3Falt%3Dmedia%26token%3Db2ec5b67-e3ac-418a-a939-5416131579f4&width=768&dpr=3&quality=100&sign=acb815e0&sv=2)

### More Color-accurate Diffuse Effect

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fzbzh2jkjIGOXukZFKgZx%252F1111.png%3Falt%3Dmedia%26token%3Ddb358e46-3648-4e50-b7b6-df9b60821898&width=768&dpr=3&quality=100&sign=57fbdaab&sv=2)

2.7 Preview

### Enhanced Ray Bounces

Optimizations to noise reduction and GI algorithms improves the lighting details. The contrast between light and shadows will be more pronounced, and the issue of abnormal brightness under sofas in previous versions has been addressed.

### More Accurate GI for Plants

### Support for Soft Shadow Reflections in Video Renderings

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FGPieqCdxtKnkwVdisoSM%252Fimage.png%3Falt%3Dmedia%26token%3Db24f503b-5f35-4a7e-85d4-aaf87ce1b5f4&width=768&dpr=3&quality=100&sign=45745261&sv=2)

Reflections of Soft Shadows in 2.7

### More Accurate GI for Light Sources

The accuracy of GI brightness and color from spotlights, projectors, and stage lights has been improved.

> Note: If ****an archive from a version prior to 2.7**** is opened in 2.7, it may appear that the "****scene becomes darker/lighting effects become weaker****". This in expected, because the effect of the previous version was inaccurate.
>
> Suggestion: Re-adjust the brightness of the light source in version 2.7 and adjust it with post parameters.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FgbOeC4t0QEsaxNn2m36j%252F2222.png%3Falt%3Dmedia%26token%3Dae802329-deec-457e-b4f2-656ed796ede9&width=768&dpr=3&quality=100&sign=83284650&sv=2)

Light sources 1, 3 and 4 are preview effects in 2.7