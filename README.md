<h1 align="center">
  Jake
</h1>

<div align="center">
  Jake is a tool that allows you to effortlessly create your one-link website and deploy it on your GitHub account.
  <br />
  <br />
  <a href="https://thevahidal.github.io/jake">Demo</a>
  <br />
  <br />
  <a href="https://thevahidal.github.io/jake">
      <img src='docs/demo.png' style="">
  </a>
</div>

## Usage

### 1. Clone Jake's Repository

To get started, follow these steps to clone Jake's repository:

1. Click [here](https://github.com/thevahidal/jake/fork) to clone Jake's repository.
2. Choose a name for your repository. If you want your website to be deployed at `<yourusername>.github.io`, name your repository `<yourusername>.github.io`. Alternatively, you can choose any other name, such as `that-other-name`, which will result in your website being deployed at `<yourusername>.github.io/that-other-name/`.

### 2. Enable GitHub Pages

After creating the repository, you need to enable GitHub Pages. Follow these steps:

1. Go to your repository's `Settings` tab.
2. Navigate to the `Pages` section.
3. Choose `GitHub Actions` as the source for your GitHub Pages.
4. Click `Save` to apply the changes.

### 3. Add your data

To customize your website, follow these steps:

1. Open your repository in your preferred text editor.
2. Locate the `data.toml` file and update it with your information.

<details>
<summary>Click to <b>Learn</b> all the available settings here</summary>

#### General Information

- `name`: Your name (e.g., "Vahid Al")
- `description`: A brief bio about yourself (e.g., "Software Developer and passionate about creating things")
- `keywords`: Keywords for the keywords meta tag (e.g., "python, javascript, go")
- `image`: The file address of your avatar. Place your avatar inside the `dist/img/` folder (e.g., "me.jpeg" - Note that the `/dist/img/` address is not included)
- `theme`: Choose your website theme: "dark" or "light" (e.g., "dark")
- `primary_color`: Specify your website's primary color using a hexadecimal color code (e.g., "#00897b")
- `text_align`: Specify the text alignment for your website: "right", "left" or "center" (e.g., "center")
- `gtag_id`: Your Google Analytics tracking ID (e.g., "G-33WB8LVHR6")
- `base_url`: The base URL for your website, mentioned in **1. Create a Repository** step (e.g., <https://thevahidal.github.io/jake>)

#### Sections

You can add multiple sections based on your requirements.
For example, you may want a section for your projects, another for your social media links, and another for your merchandise products.

Each section is defined using `[[sections]]` and has the following components:

- `title`: The title of the section (e.g., "Projects")
- `description`: A brief description of the section (e.g., "Here are some of my projects")
- `direction`: The direction of the section: "row" or "column" (e.g., "row")
- `item_style`: The style of the items in the section: "outline" or "filled" (e.g., "outline")
- `items`: The items associated with the section.

#### Items

Each item is defined using `[[sections.items]]` and has the following components:

- `title`: The title of the item (e.g., "Soul")
- `description`: A brief description of the item (e.g., "An SQLite REST and Real-time server")
- `url`: The URL associated with the item (e.g., "<https://github.com/thevahidal/soul>")

</details>

### 4. Voila

That's all you need to do. Now, you can sit back and relax while your website gets deployed. You can monitor the progress in the `Actions` tab of your repository. Once the deployment is complete, you can access your brand new one-link website at `<yourusername>.github.io` (If you chose `<yourusername>.github.io` as your repository name) or `<yourusername>.github.io/repo-name/`.

### FAQ

<details>
<summary>1. How to configure my own <b>Custom Domain</b>?</summary>

If you want to use your custom domain for your website hosted on GitHub Pages, it's a straightforward process. Just follow these steps:

1. Go to the **Settings** tab of your GitHub repository.
2. Select **Pages** tab in the sidebar.
3. Under the **Custom domain** section, enter your desired domain name.
4. Click **Save**.

That's it! Your GitHub Pages site will now be accessible using your custom domain.

For more detailed instructions and information on using a custom domain with GitHub Pages, you can refer to the [official GitHub Docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site).

</details>

<details>
<summary>2. How to <b>manually</b> trigger the GitHub Action to deploy my website?</summary>

1. In your repository, navigate to the "Actions" tab.
2. Look for the workflow named "Deploy Jake Website to GitHub Pages" in the list of workflows.
3. If you see an alert stating "This workflow has a workflow_dispatch event trigger," it means you can manually trigger the workflow.
4. Click on the "Run Workflow" button. A new window will appear.
5. Within the new window, click on the green "Run Workflow" button.
6. GitHub Actions will initiate the deployment process for your static content to GitHub Pages.

</details>

<details>
<summary>3. How to <b>update</b> my repository with the latest version of Jake?</summary>

Since Jake is a template repository, users who create repositories from it won't automatically receive updates when changes are made to the original template. To update your repository with the latest changes while preserving your custom data (such as the `data.toml` file), follow these steps:

1. **Create a backup of your custom data:**

   - Before updating, make sure to back up the `data.toml` file or any other files that contain your specific customizations, as these may be overwritten during the update process.

2. **Sync with the latest version of Jake:**

   - In your repository, click on the "GitHub Desktop" or use the command line to fetch the latest changes from the original template.
   - You can do this by adding the original repository as a remote:

     ```bash
     git remote add upstream https://github.com/thevahidal/jake.git
     git fetch upstream
     git merge upstream/main
     ```

   - This will merge the latest changes from the Jake template into your repository.

3. **Resolve any conflicts:**

   - If there are conflicts, especially in files like `data.toml`, you’ll need to manually merge the updates from the template with your custom data. The `data.toml` file is where your personal data is stored, so be careful not to overwrite your custom settings.

4. **Push the changes:**

   - Once you've resolved any conflicts, commit the changes and push them back to your repository.

5. **Review your site:**
   - After updating, review your website to ensure everything is still functioning as expected. You can monitor the progress of the update in the "Actions" tab of your repository.

By following these steps, you can ensure that your repository stays up to date with the latest improvements from the Jake template while preserving your personal customizations.

</details>

### Jake's Friends

Here’s a growing list of awesome people using **Jake**!  

- [thevahidal](https://thevahidal.github.io/) – [thevahidal/thevahidal.github.io](https://github.com/thevahidal/thevahidal.github.io)

Want to be featured here? Just open a pull request and add your site to the end of the list using the format below:

```
- [Your Website Name](Your Website URL) – [YourUsername/YourRepo](https://github.com/YourUsername/YourRepo)
Example:
- [thevahidal](https://thevahidal.github.io/) – [thevahidal/thevahidal.github.io](https://github.com/thevahidal/thevahidal.github.io)
```

### Local Development

If you'd like to test or customize this project locally without triggering GitHub Actions, follow the steps below to set up and run the pipeline on your machine.

#### Prerequisites

Ensure the following are installed:

- [Python 3.11+](https://www.python.org/)
- [Poetry](https://python-poetry.org/) (You can install Poetry via [pipx](https://pypa.github.io/pipx/): `pipx install poetry`)

#### Steps for Local Development

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/jake.git
cd jake
```

2. Install dependencies using `Poetry`:

```bash
poetry install --no-root
```

3. Run the generator script: This will generate the HTML files and output them to the `dist/` directory.

```bash
poetry run python script.py
```

4. Preview your changes: Open the generated HTML files in your browser or use a local server to serve the dist folder:

```bash
python -m http.server --directory dist 8000
```

Then, open [http://localhost:8000](http://localhost:8000) in your browser.

#### Optional: Build Automation Script

To simplify these steps, you can use the provided `local_run.sh` script. This script will automate the process.

Make the script executable:

```bash
chmod +x local_run.sh
```

Run it without arguments for a one-time build and serve:

```bash
./local_run.sh
```

Run it with the `--watch` flag to enable development mode with hot reload (rebuilds automatically when files change):

```bash
./local_run.sh --watch
```

## Contributing

If you find any issues or have suggestions for improvement, please feel free to contribute by submitting a pull request or creating an issue in the repository.

## License

This project is licensed under the [MIT License](LICENSE).
