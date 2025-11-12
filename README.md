
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20617640)

## To get the latest updates:

1. **Fetch From All Remotes**: Source Control -> More Actions... -> Pull, Push -> Fetch From All Remotes

![Step 1](assets/git-1.png "Source Control -> More Actions... -> Pull, Push -> Fetch From All Remotes")

2. **Merge**: Source Control -> More Actions... -> Branch -> Merge

![Step 2](assets/git-2.png "Source Control -> More Actions... -> Branch -> Merge")

3. **Select branch** upstream/HEAD

![Step 3](assets/git-3.png "upstream/HEAD")

Main Project:
    Approach:
        I wanted to make a program that would present options for you to choose from and for it to print onto the screen. I wanted atleast 1 to be customizable.
    Explanation:
        Program lets user choose between drawing a pumpkin, snowflake or tree. If tree is chosen it lets user choose the amount of branches and the season they want it to be.

    Testing Log:
    Pumpkin is slightly off center but looks good
    Snowflake is drawn very slowly, increasing the speed
    Tree is hard to implement with the others
    Asking for the amount of branches is causing issues when tree isn't chosen
    Finally got

    Recursive approach for the tree:
    keeps dividing the size of the branches so it visably looks smaller each time it branches out

    Input:
    pumpkin
    Output:
    *prints pumpkin drawing*
    Input:
    snowflake
    Output:
    *prints snowflake drawing*
    Input:
    tree
    5
    Output:
    *prints tree drawing with 5 different branches*

    Challenges in Development:
    - Trouble with asking for amount of branches even when tree wasn't chosen
    - Trouble with tree getting crunched into a ball
    - Trouble with ideas
    
    Peer evaluation:
        Pretty good except limited freedom when making pumpkin and snowflake, if leland added editable levels for the snowflake and make the pumpkin bigger or smaller, it would be better.

        -Karson

