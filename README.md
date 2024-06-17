# Repo Milestone Visualizer
Show the milestone of your repo.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Harshit2012/Repo-Milestone-Visualizer?tab=MIT-1-ov-file#readme)
![GitHub Release](https://img.shields.io/github/v/release/harshit2012/Repo-Milestone-Visualizer)
![Forks](https://img.shields.io/github/forks/harshit2012/Repo-Milestone-Visualizer)
![Stars](https://img.shields.io/github/stars/harshit2012/Repo-Milestone-Visualizer)

## Fetures
- Easy to use
- One click fetch the data and download

## Technologies Used
<code><img width="51" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/></code>

## How it works?
1. When enter the username and repo-name and click on `fetch data and download chart button` it will get the data using github api and download in in `.png` format.
2. It create charts of pull requests, commits, stars, forks, issues and watchers.
3. Each chart has a title that changes based on the metric value, categorized into "low," "medium," and "high" ranges with corresponding labels. For example:
   - Stars: "Rising Star," "Popular," "Star Struck!"
   - Forks: "Just Started," "Fork-tastic," "Fork Legend"
   - Issues: "Few Issues," "Some Issues," "Issue Magnet"
   - Watchers: "Some Watchers," "Watching Closely," "Highly Watched"
   - Pull Requests: "Few PRs," "Active PRs," "24x7 Puller"
   - Commits: "Few Commits," "Regular Commits," "Commit King"

## Example
**Repository:- Repo-Milestone-Visualizer**
![graph](https://github.com/Harshit2012/Repo-Milestone-Visualizer/assets/105143145/2022ac38-6bd0-4204-bf56-f5141fc75724)

## Adding it to readme
Drag the chart and drop in readme or use img tag.
### img tag
```markdown
<img src="path/to/your/saved/graph.png" alt="Repo Milestones" style="max-width: 100%; height: auto;">
```

## To install libraries
### Tkinter
```bash
pip install tkinter
```

## To run
```bash
python repo_milestone_visualizer.py
```

## Contribution
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.

## License
This repository is licensed under [MIT License](https://github.com/Harshit2012/Repo-Milestone-Visualizer#MIT-1-ov-file)
