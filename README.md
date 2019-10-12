# techedits

This little bot will watch Wikipedia for edits from an IP address from one of the world's largest tech companies and will [tweet](https://twitter.com/techedits) when it notices one.

You can find the list of companies under watch listed below.

Inspired and powered by [anon](https://github.com/edsu/anon).

## Pull Requests

Feel free to raise a pull request to add additional companies. Use the below format in [ranges.yaml](ranges.yaml).

    mycompanyname:
    # ASN num
    - 143.231.0.0/22

These will be converted into [ranges.json](ranges.json) and listed below once deployed to the bot.

## Finding / Confirming IP Ranges

You can search for banks to find their ASNs and IP ranges using [this tool from Hurricane Electric](https://bgp.he.net/).

You can also cross reference with this [ASN Lookup Tool](https://www.ultratools.com/tools/asnInfoResult). 

The ASN used to discover IP ranges are listed in [ranges.yaml](ranges.yaml) as comments. 

## List of Companies

* Atlassian
* Google
* Microsoft
* Netflix
* Twitter
* YouTube
