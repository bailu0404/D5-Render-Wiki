# Team Group Management

⚠ This particular feature is designed for teams seeking to secure seat licenses en masse and manage several groups on a separate basis. If you need to activate this feature, please contact our staff at [[email protected]](https://docs.d5render.com/cdn-cgi/l/email-protection).

The activation of Group Management is recommended if your team has:

- Groups working at different places that cannot deploy the same Local Area Network (LAN) server address
- Groups responsible for individual projects that require prevention from cross-group visibility

For now, each team member has a team role such as Owner, Admin, or Member. When Group Management is enabled, members will have an additional group role.

- A group has its own group Admins and group Members.
- A team member can join multiple groups.
- A group has its individual D5 Studio space, project library, and asset library.

**\*A team member could have a team role and a group role at the same time.**

### Create a Group

The Owner of a team could see the 'Group Management' panel after logging into the team management board.

Click on 'Create a Group' and fill in the necessary info to create a new group. Please note that only the team Owner could create or delete groups.

When a group is deleted, the following data stored in the D5 server would also be deleted:

**Please note that deleting a group won't remove members from the team, but only from the group.**

### How to Invite Group Members

The Team Owner will automatically join the group after it's created. The Team Owner could remove him/herself from the group as well. Whether in the group or not, the Team Owner has full control over all groups, including inviting/removing members and setting group roles.

There are two ways to invite a group member:

**Generally speaking, the total number of group members should not exceed the team's available seats. At present, we do not support specifying invitation quotas for specific groups.**

### Group Roles

The Team Owner could set one or more administrators for a group.

Please note that

RolesAuthority

Owner

- Creat groups
- Delete groups
- Set group roles
- All the management authorities of Group Admin

Group Admin

- Visit the Team management board
- Visit the 'Members' panel of the Team management board, but can't make any operations
- Visit the 'Group Management' panel, which is only accessible to group admins and the Team Owner
- Manage the group which the admin is appointed to

****Group Member Management****

- Invite non-team members to join the team and the group
- Invite team members to join the group
- Remove members from the team and the group
- Remove members only from the group

****Group Resource Management****

Visit and manage

- Group library
- Group Studio space
- Group cloud projects

Super Group Admin (1 person only)

The difference between Super Group Admin and Group Admin is:

- Super Group Admin can change 【Account Attributes (Editable, Manage-only)】 within Group

Group Member

Visit

- Group library
- Group Studio space
- Group cloud projects

The accessibility of different panels of the team management board is as follows:

MembersGroupBilling & PlansTeam DetailsTeam LibraryCloud StorageTeam Report

Owner

✅

✅

✅

✅

✅

✅

✅

Team Member

Team Admin

✅

✅

✅

✅

✅

Group Member

Group Admin

✅
(Only able to edit the info of the admin's own group)

✅
(Access to view team info; editing not permitted)

✅

✅

### How to Remove Group Members

There are two ways to remove group members.

### How to Access Group Resources in D5 Render

Group members will see all the groups they have joined after logging into the Team account in D5 at the welcome page. Group members have to select the group they need to access the corresponding group resources. Upon the next login, the previously selected group will be chosen by default.

**Please note that the Team Space is a default group available to every team member.**

### Group Management Mode

#### Group Management Mode Introduction

Based on the customer's requirements, teams with the group management feature enabled can select from two different group management modes:

- ****Normal Mode(default):**** A member can join multiple groups simultaneously, which is suitable for scenarios where a team has several projects with overlapping group members.
- ****Independent Mode:**** Each group needs to be assigned available seats, and the sum of the available seats for all groups must not exceed the total number of seats in the team; a member can only join a maximum of one group (except for members with the “Manage Only” attribute). Ideal for large companies managing multiple subsidiaries.

Difference between two modes:

Normal ModeIndependent Mode

1

Groups can have unlimited seats (as long as it doesn't exceed the number of team seats)

Each group must be assigned seat limit

2

The seat number for one group can't exceed the total seats for the team

The total number of seats for all groups can't exceed the total seats for the team

3

After limiting seats, the vacant seats in the group have no effect on the remaining available seats for the team

Vacant seats within each group also occupy team seats

4

A member can be in multiple groups

A member can only be in one distinct group (except for the 'Manage-only' attribute account)

#### ****Group Management Mode Change****

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FuBV5tqGCn1JT8Biqb9Wh%252Fimage.png%3Falt%3Dmedia%26token%3D32f172de-f0e3-4f1b-95da-50cd095b7cc0&width=768&dpr=3&quality=100&sign=1ef58185&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FyuYm2Tybelh8Evbcjtun%252Fimage.png%3Falt%3Dmedia%26token%3D80d9fa50-122d-48f8-8620-176e46c26335&width=768&dpr=3&quality=100&sign=b5343720&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FDWYYdLKqMTtMrhC1rgYy%252Fimage.png%3Falt%3Dmedia%26token%3Ddf79f894-bcf1-4ea4-a70b-db86a4a7d1a7&width=768&dpr=3&quality=100&sign=d8a68c95&sv=2)

a. If a member belongs to multiple groups, you can choose which group to retain them in using the drop-down menu. Once the selection is made, the member will be removed from all other groups. (Members with the "Manage only" attribute are exempt from this restriction.)

b. When there are groups haven't been assigned seats or the total number of seats assigned to all groups exceeds the total seat number for the team, it can be adjusted directly in the pop-up window.

c. Once the above modifications are completed, the group management mode will be successfully switched to ****Independent Mode****.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252F3aSEsRFUE1RNHs8WoGur%252Fimage.png%3Falt%3Dmedia%26token%3D8de35a27-6d99-4ea6-b110-e98934cb4885&width=768&dpr=3&quality=100&sign=e3eadfc0&sv=2)![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FdaJdJiM2FgtSbIZjpI1n%252Fimage.png%3Falt%3Dmedia%26token%3D0196b73a-6eb3-4614-960c-6e6fe3c3b8eb&width=768&dpr=3&quality=100&sign=58d2b9ae&sv=2)

#### ****Group Management under Independent Mode****

In Independent Mode, the group management page will be changed from ****Card**** to ****List****, which is convenient for administrators to view the currently assigned seats and used seats of each group.

![](https://docs.d5render.com/~gitbook/image?url=https%3A%2F%2F3611830798-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MjbN1iGmN_HBnj_fyU9%252Fuploads%252FPAR3TylTI9PZDsc5L9nQ%252Fimage.png%3Falt%3Dmedia%26token%3D83474070-6898-49a4-9f91-713adb5a58f6&width=768&dpr=3&quality=100&sign=94e0b6de&sv=2)