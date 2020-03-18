# IIIF Registry
This is the basis of the IIIF Registry of Activity streams. This project aims to give access to a large amount of IIIF resources and provide a way to keep up to date with changes. The Activity Streams format is defined in the [Change Discovery Specification](https://iiif.io/api/discovery/0.4/).

We welcome additions to the registry and additions can be made using the following process:

  1. Create branch for your addition
  2. Create a directory for your institution. This should be a short name without spaces or punctuation
  3. Create a registry JSON file. See details below
  4. Create a pull request with your changes and submit to IIIF/registry

## Registry JSON format  

To register a link to your streams we use the following JSON structure: 

```
{
    "id": "http://www.getty.edu/",
    "institution": "Getty",
    "streams": [
        {
            "id": "http://www.getty.edu/museum.json",
            "label": "Museum collections" 
        },
        {
            "id": "http://www.getty.edu/library.json",
            "label": "Library collections" 
        },
        {
            "id": "http://www.getty.edu/research.json",
            "label": "Research Center" 
        }
    ]
}
```

Where:
 * `id` is a URI for your institution. This could be an institution website, Wikidata URI or other resolvable link. 
 * `institution` the name of the institution that could be shown to a user
 * `streams` list of activity streams for this institution
    * `id` Activity Stream URL. Must be resolvable 
    * `label` a description that can be shown to the user so they can tell which stream to monitor for updates. 

The JSON file should be named appropriately so people know what it represents and must have an extension of `.json`.

## Aggregators

For Aggregators or institutions that collect content from other providers and aggregate their content. A slightly different structure can be used. Examples of Aggregators would be Europeana or OCLC with ContentDM. Both hold multiple institutions' data. In this case the Aggregator would have one registry JSON file per institutional client. The Provider can then add the following to the root of the JSON to show who provided the content:

```
"provider": {
    "id": "https://www.oclc.org/en/home.html",
    "label": "OCLC"
},
```

You can see examples of this in the [OCLC directory](https://github.com/IIIF/registry/tree/deploy/OCLC) where [instx.json](https://github.com/IIIF/registry/blob/deploy/OCLC/instx.json) would be the set of changes from one ContentDM instance and [insty.json](https://github.com/IIIF/registry/blob/deploy/OCLC/insty.json) is a second institution. 
