import matplotlib.pyplot as plt
import seaborn as sns  # optional, if you want to use Seaborn's style
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.patches as mpatches

sns.set_style("white")

age_groups = [
    {'label': '-18', 'count': 4, 'color': 'lightblue', 'percentage': '8%', 'png_path': 'human_lightblue.png'},
    {'label': '18-25', 'count': 24, 'color': 'green', 'percentage': '47%', 'png_path': 'human_green.png'},
    {'label': '25-35', 'count': 4, 'color': 'yellow', 'percentage': '4%', 'png_path': 'human_yellow.png'},
    {'label': '35-50', 'count': 8, 'color': 'orange', 'percentage': '16%', 'png_path': 'human_orange.png'},
    {'label': '50+', 'count': 11, 'color': 'red', 'percentage': '22%', 'png_path': 'human_red.png'},
]

# Sum up how many icons total
total_icons = sum(g['count'] for g in age_groups)

# Number of icons per row
icons_per_row = 20

# Figure setup
fig, ax = plt.subplots(figsize=(10, 5))


# Helper function to load each PNG and wrap in an OffsetImage
def load_icon(png_path, zoom=0.35):
    img = plt.imread(png_path)  # Must be PNG/JPG; cannot be raw SVG here
    return OffsetImage(img, zoom=zoom)


# We'll place icons row by row
x_coord = 0
y_coord = 0

for group in age_groups:
    icon_img = load_icon(group['png_path'], zoom=0.35)

    for i in range(group['count']):
        # Compute grid position
        x = x_coord % icons_per_row
        y = -(x_coord // icons_per_row)  # negative for downward rows
        x_coord += 1

        # Create annotation for each icon
        ab = AnnotationBbox(icon_img, (x, y), frameon=False)
        ax.add_artist(ab)

# Create the legend
# Even though icons are colored individually via PNG files, we use patches
# to display the color-coded legend entries:
patches = [
    mpatches.Patch(color=g['color'], label=f"{g['label']} ({g['percentage']})")
    for g in age_groups
]
ax.legend(handles=patches, loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=5)

# Adjust view limits to fit all icons comfortably
num_rows = (total_icons // icons_per_row) + 1
ax.set_xlim(-1, icons_per_row + 1)
ax.set_ylim(-num_rows, 1)

# Hide axes
ax.axis('off')

# Add a title or any additional text
ax.set_title("Faixa etária - 53 pessoas", fontsize=14)

# Final layout and display
plt.tight_layout()
plt.show()
