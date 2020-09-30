---
title: IIIF Registry
layout: default
tags: [tbc]
summary: "tbc"
---

# IIIF Registry
This is the IIIF Registry of Activity Streams. This project aims to give access to a large amount of IIIF resources and to achive this the IIIF Registry maintains a link to institution ActivityStreams. ActivityStreams can provide a way of sycnhronising changes to IIIF manifests by providing notifications of changes. The IIIF Registry aims to be the top level collection of Activity Streams for the IIIF Community. You can access the registry at the following URL:

[https://registry.iiif.io/index.json](https://registry.iiif.io/index.json)

The Activity Streams format both for the registry and linked assets is defined in the [Change Discovery Specification](https://iiif.io/api/discovery/0.4/). We welcome additions to the registry and they can be made using the following process:

  1. Create branch for your addition in the [registry GitHub](https://github.com/IIIF/registry) 
  2. Create a directory for your institution. This should be a short name without spaces or punctuation
  3. Create a registry JSON file. See details in the GitHub [README.md](https://github.com/IIIF/registry)
  4. Create a pull request with your changes and submit to IIIF/registry
