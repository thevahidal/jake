# Jake

Jake is a tool that allows you to effortlessly create your own one-link website and deploy it on your GitHub account.

## Usage

### Create a Repository
To get started, follow these steps to create a new repository using this template:

1. Click [here](https://github.com/new?template_name=jake&template_owner=thevahidal) to create a new repository.
2. Choose a name for your repository. If you want your website to be deployed at `<yourusername>.github.io`, name your repository `<yourusername>.github.io`. Alternatively, you can choose any other name, such as `that-other-name`, which will result in your website being deployed at `<yourusername>.github.io/that-other-name/`.

### Enable GitHub Pages
After creating the repository, you need to enable GitHub Pages. Follow these steps:

1. Go to your repository's `Settings` tab.
2. Navigate to the `Pages` section.
3. Choose `GitHub Actions` as the source for your GitHub Pages.
4. Click `Save` to apply the changes.

### Add your data
To customize your website, follow these steps:

1. Open your repository in your preferred text editor.
2. Locate the `data.toml` file and update it with your own information.
3. Modify the following settings according to your preferences:

**General Information:**
- `name`: Your name (e.g., "Vahid Al")
- `description`: A brief bio about yourself (e.g., "Software Developer and passionate about creating things")
- `keywords`: Keywords for the keywords meta tag (e.g., "python, javascript, go")
- `image`: The file address of your avatar. Place your avatar inside the `dist/img/` folder (e.g., "me.jpeg" - Note that the `/dist/img/` address is not included)
- `theme`: Choose your website theme: "dark" or "light" (e.g., "dark")
- `primary_color`: Specify your website's primary color using a hexadecimal color code (e.g., "#00897b")

**Sections:**
You can add multiple sections based on your requirements. For example, you may want a section for your projects, another for your social media links, and another for your merchandise products. Each section is defined using `[[sections]]`.

Each section has the following components:
- `title`: The title of the section (e.g., "Projects")
- `description`: A brief description of the section (e.g., "Here are some of my projects")
- `items`: The items associated with the section. Each item is defined using `[[sections.items]]`.

Each item within a section has the following components:
- `title`: The title of the item (e.g., "Soul")
- `description`: A brief description of the item (e.g., "An SQLite REST and Real-time server")
- `url`: The URL associated with the item (e.g., "https://github.com/thevahidal/soul")

Make the necessary modifications to the `data.toml` file based on the above instructions to customize your website with your own information and sections.

### Voila!
That's all you need to do. Now, you can sit back and relax while your website gets deployed. You can monitor the progress in the `Actions` tab of your repository. Once the deployment is complete, you can access your brand new one-link website at `<yourusername>.github.io` or `<yourusername>.github.io/repo-name/`.

Feel free to customize your website by modifying the code and adding your own content.

## Contributing
If you find any issues or have suggestions for improvement, please feel free to contribute by submitting a pull request or creating an issue in the repository.

## License
This project is licensed under the [MIT License](LICENSE).
