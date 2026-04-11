# How to edit plants created by brushes

You can hide/delete/re-edit again by the brush records, which can be used as follows:

After using the Brush or Scatter tool to draw plants on a model, selected models will display brush records in the right sidebar when the models are unlocked. Hover over the asset thumbnail to see the specific names of the assets. Each brush record can be hidden.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fat53DpyDqPqyVq99j4hy%252Fbrush%2520record.jpg%3Falt%3Dmedia%26token%3D091db924-5715-421e-acef-62b88b6ab6e8&width=768&dpr=3&quality=100&sign=286a2b20&sv=2)

The brush record contains information about the plants drawn, and also supports applying the plants in the current record to the brush and eraser. Plants in the record can be continued to be drawn or erased. Right click on the brush record, you can delete it to manage the material in the scene more conveniently.

## Combination of brush records

Each time you draw, if you select the same plant, it will be merged into one record. If the first brush draws three plants A/B/C, the second brush draws three plants B/C/D, and the third brush continues to draw three plants A/B/C, then there are only two brush records for this model: A/B/C and B/C/D . That is, the first and the third brush painted the same plants, which are combined into one record.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252Fo4cmd67XJd8NFO4eOnKm%252Fbrush%2520record%25202.jpg%3Falt%3Dmedia%26token%3D1a9ef2be-521e-4cf4-a935-d8b520155299&width=768&dpr=3&quality=100&sign=a0f58c54&sv=2)

Currently, plants drawn with tools (Brush/Spread/Path) do not support the operation of "editing or deleting one of them individually", but only support the use of eraser to remove or the use of brush records to manage the drawn plants as a whole. We will consider adding this feature in future releases.

## Common issues

### How to delete the plants?

When a model with brush/scatter plant load is selected, the right sidebar will show the corresponding brush records, and you can right-click to delete the records. If the same plant is selected for each brush paint, it will be merged into the same brush record.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FgaJ8Z4HcGZQutvLKxh7m%252Fbrush%2520delete.jpg%3Falt%3Dmedia%26token%3D08b93b14-afe9-4ebd-8acd-a560074c8593&width=768&dpr=3&quality=100&sign=756a193c&sv=2)

Plants placed using the Path tool will be displayed in the Objects on the left and can be selected and then deleted.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FQmkXGt0osDOdmCutkCye%252Fpath%2520delete.jpg%3Falt%3Dmedia%26token%3Dc264c153-f76d-4a73-a781-ba1748e20fb5&width=768&dpr=3&quality=100&sign=9025d863&sv=2)

Plants placed individually are shown in Objects on the left and can be selected and then deleted.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FSzEyPE7tqcp0b8h8Ye9l%252Findividual%2520delete.jpg%3Falt%3Dmedia%26token%3Dc4e6f5ea-31b9-4609-8c3a-fd326002d101&width=768&dpr=3&quality=100&sign=b4d5f477&sv=2)