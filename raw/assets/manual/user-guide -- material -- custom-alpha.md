# What materials are the Custom Alpha templates suitable for? What are the special parameters?

The only special parameter of this template is the "Opacity Map" parameter. But there is a slight difference with the "Opacity Map" in the Cloth material template. There is no semi-transparent effect here, the material is either ****completely preserved or completely hollow****.

Therefore, here it is recommended to use only black and white map to control the hollow effect.

- White is the material that is preserved, and black corresponds to the hollow position.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-MjbN1iGmN_HBnj_fyU9%252F-Mkeq_gBgXvtoU8OUgdO%252F-Mker6UJPFSjcsgLKwHY%252Falph.gif%3Falt%3Dmedia%26token%3Df7f8c645-793d-47f6-a89e-b8fd423f309e&width=768&dpr=3&quality=100&sign=a3c4b4f6&sv=2)
> ℹ️ > In the range of 0~255, Opacity Map gray value greater than 157, the corresponding material will be retained, and gray value less than 156, the corresponding material will be hollowed out.