import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import requests
import matplotlib.pyplot as plt
import numpy as np

class RepoMilestoneVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Repo Milestone Visualizer")
        
        self.setup_gui()

    def setup_gui(self):
        heading = tk.Label(self.root, text="Repo Milestone Visualizer", font=("Arial", 24))
        heading.pack(pady=10)

        subheading = tk.Label(self.root, text="Enter GitHub username and repository name", font=("Arial", 14))
        subheading.pack(pady=5)

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(form_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Repository:").grid(row=1, column=0, padx=5, pady=5)
        self.repo_entry = tk.Entry(form_frame)
        self.repo_entry.grid(row=1, column=1, padx=5, pady=5)

        fetch_button = tk.Button(self.root, text="Fetch Data and Download Chart", command=self.fetch_and_download)
        fetch_button.pack(pady=10)

    def fetch_and_download(self):
        username = self.username_entry.get()
        repo = self.repo_entry.get()
        if not username or not repo:
            messagebox.showerror("Input Error", "Please enter both username and repository name.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if not file_path:
            return

        try:
            url = f"https://api.github.com/repos/{username}/{repo}"
            response = requests.get(url)
            if response.status_code == 404:
                messagebox.showerror("Error", "Repository not found.")
                return
            elif response.status_code == 403:
                messagebox.showerror("Error", "GitHub API rate limit reached. Please try again later.")
                return
            elif response.status_code != 200:
                messagebox.showerror("Error", f"Failed to fetch data from GitHub. Status code: {response.status_code}")
                return

            data = response.json()
            stars = data.get('stargazers_count', 0)
            forks = data.get('forks_count', 0)
            issues = data.get('open_issues_count', 0)
            watchers = data.get('watchers_count', 0)

            pr_url = f"https://api.github.com/repos/{username}/{repo}/pulls?state=all"
            pr_response = requests.get(pr_url)
            if pr_response.status_code == 403:
                messagebox.showerror("Error", "GitHub API rate limit reached. Please try again later.")
                return
            pull_requests = len(pr_response.json())

            commits_url = f"https://api.github.com/repos/{username}/{repo}/commits"
            commits_response = requests.get(commits_url)
            if commits_response.status_code == 403:
                messagebox.showerror("Error", "GitHub API rate limit reached. Please try again later.")
                return
            commits = len(commits_response.json())

            self.create_and_save_charts(file_path, stars, forks, issues, watchers, pull_requests, commits)
            messagebox.showinfo("Success", f"Chart saved to {file_path}")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Network error: {e}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_label(self, metric_name, value):
        thresholds = {
            "Stars": [50, 200],
            "Forks": [20, 100],
            "Issues": [10, 50],
            "Watchers": [10, 50],
            "Pull Requests": [5, 20],
            "Commits": [50, 200]
        }

        labels = {
            "Stars": ["Rising Star", "Popular", "Star Struck!"],
            "Forks": ["Just Started", "Fork-tastic", "Fork Legend"],
            "Issues": ["Few Issues", "Some Issues", "Issue Magnet"],
            "Watchers": ["Some Watchers", "Watching Closely", "Highly Watched"],
            "Pull Requests": ["Few PRs", "Active PRs", "24x7 Puller"],
            "Commits": ["Few Commits", "Regular Commits", "Commit King"]
        }

        low, medium = thresholds[metric_name]
        if value < low:
            return labels[metric_name][0]
        elif value < medium:
            return labels[metric_name][1]
        else:
            return labels[metric_name][2]

    def create_and_save_charts(self, file_path, stars, forks, issues, watchers, pull_requests, commits):
        data = {
            "Stars": stars,
            "Forks": forks,
            "Issues": issues,
            "Watchers": watchers,
            "Pull Requests": pull_requests,
            "Commits": commits
        }

        fig, axs = plt.subplots(3, 2, figsize=(10, 8))
        fig.suptitle("GitHub Repository Milestones", fontsize=16)
        fig.subplots_adjust(hspace=0.5)

        for i, (key, value) in enumerate(data.items()):
            ax = axs[i//2, i%2]
            ax.bar(key, value, color=np.random.rand(3,))
            ax.set_title(self.get_label(key, value))
            ax.set_ylabel('Count')

        fig.savefig(file_path)
        plt.close(fig)

if __name__ == "__main__":
    root = tk.Tk()
    app = RepoMilestoneVisualizer(root)
    root.mainloop()