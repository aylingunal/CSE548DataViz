four_charts_template = """
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdn.jsdelivr.net/npm/vega@{vega_version}"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@{vegalite_version}"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@{vegaembed_version}"></script>
</head>
<body>

<div id="vis1"></div>
<div id="vis2"></div>
<div id="vis3"></div>
<div id="vis4"></div>

<script type="text/javascript">
  vegaEmbed('#vis1', {spec1}).catch(console.error);
  vegaEmbed('#vis2', {spec2}).catch(console.error);
  vegaEmbed('#vis3', {spec3}).catch(console.error);
  vegaEmbed('#vis4', {spec4}).catch(console.error);
</script>
</body>
</html>
"""

with open("combined.html", "w") as f:
    f.write(
        four_charts_template.format(
            vega_version=alt.VEGA_VERSION,
            vegalite_version=alt.VEGALITE_VERSION,
            vegaembed_version=alt.VEGAEMBED_VERSION,
            spec1=final_vis1.to_json(
                indent=None
            ),  # final_vis1 is the name of the first chart
            spec2=final_vis2.to_json(
                indent=None
            ),  # final_vis2 is the name of the second chart
            spec3=final_vis3.to_json(
                indent=None
            ),  # final_vis3 is the name of the third chart
            spec4=final_vis4.to_json(
                indent=None
            ),  # final_vis4 is the name of the fourth chart
        )
    )
