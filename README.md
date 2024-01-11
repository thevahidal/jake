<h1 align="center">
    <a href="https://github.com/thevahidal/jake">
        <img src='docs/logo.jpeg' height='200px' style="">
    </a>
</h1>

<div align="center">
  Jake is a tool that allows you to effortlessly create your one-link website and deploy it on your GitHub account.
  <br />
  <br />
  <a href="https://thevahidal.github.io/jake">Demo</a>
</div>

## Usage

### 1. Create a Repository

To get started, follow these steps to create a new repository using this template:

1. Click [here](https://github.com/new?template_name=jake&template_owner=thevahidal) to create a new repository.
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
- `base_url`: The base URL for your website, mentioned in **1. Create a Repository** step (e.g., https://thevahidal.github.io/jake)

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
- `url`: The URL associated with the item (e.g., "https://github.com/thevahidal/soul")

</details>

### 4. Voila!

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

## Contributing

If you find any issues or have suggestions for improvement, please feel free to contribute by submitting a pull request or creating an issue in the repository.

## License

This project is licensed under the [MIT License](LICENSE).
