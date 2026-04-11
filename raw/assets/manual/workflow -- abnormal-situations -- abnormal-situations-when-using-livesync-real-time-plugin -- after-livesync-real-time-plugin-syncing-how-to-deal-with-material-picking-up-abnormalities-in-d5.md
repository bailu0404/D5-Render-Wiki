# After LiveSync(real-time plugin) syncing, how to deal with material picking up abnormalities in D5?

### Why when using SU and other LiveSyncs, partial models experience abnormal material picking up?

> ℹ️ > ****This problem has been fixed in 2.8 version of D5 Render****  (i.e. no need to do the followings can still pick up materials normally).

- If you still have the problem of can't pick up materials when using live sync plugins, but it's fine if disconnecting the connection , please check with the official technical supports.

Why is it that when using SU and other live workflow plugins, some of the models are abnormally sucked up after being synced to D5, but it is normal to absorb materials when D5 directly reads the .skp models or when using non-live version of plugins to link/convert live models to non-live?

A known issue in current version 2.5/2.6: If an individual model is scaled to be extremely small, but the boundingbox is very large, it will cause the abnormality of absorbing textures in D5 in real time.

Suggestions:

- Use version 2.6.1, add and save corresponding fields in D5Config-config.ini;
- Re-synchronize the model using the real-time plugin. The model with the abnormal boundingbox size will be displayed in D5;
- Delete the model with the abnormal boundingbox size in the modelling software and sync the model modification to D5, then it can be absorbed normally.

We will fix the issue in subsequent releases.

> - Path of config.ini file: Search for %appdata% in the Windows taskbar and enter to display the D5Config folder, and find the config.ini file under the folder with the most recent modification time.
>
> For example `C:\Users\Administrator\AppData\Roaming\D5Config`
>
> - Corresponding fields needed to be added:
>
> `[Debug]`
>
> `VerySmallScale=1`

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FY8GDQtBHUGtRFMj6y560%252Fimage.png%3Falt%3Dmedia%26token%3Dc478ab0f-adee-41eb-9b39-d90c62545cfc&width=768&dpr=3&quality=100&sign=ae0a0361&sv=2)

Path to config.ini file to be modified and fields to be added