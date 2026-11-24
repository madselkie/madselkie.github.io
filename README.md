# madselkie.com

Single static document. No build step, no framework, no dependencies, no client JavaScript.
Open index.html directly in a browser and it works.

## Deploy
GitHub Pages serves branch main, root. Edit, commit, push; Pages redeploys in about a minute.

## Custom domain (pending)
madselkie.com currently resolves to a registrar parking page. To point it here:

Apex A records, all four:
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153

www CNAME:
the-meyiwa.github.io   (this org, so: madselkie.github.io)

Or, if the registrar offers ALIAS/ANAME at the apex, point it at madselkie.github.io instead of the A records.

Add a file named CNAME containing madselkie.com only after DNS resolves, then enable Enforce HTTPS in
Settings > Pages. Adding it first takes the .github.io address down as well.
