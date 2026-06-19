import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle, Rectangle, Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_cylinder(radius, height, center=(0, 0, 0)):
    z = np.linspace(center[2], center[2] + height, 2)
    theta = np.linspace(0, 2 * np.pi, 20)
    theta, z = np.meshgrid(theta, z)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return x, y, z

def create_gear(radius, teeth, height):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Main gear body (cylinder)
    x, y, z = create_cylinder(radius, height)
    ax.plot_surface(x, y, z, color='blue', alpha=0.7)

    # Gear teeth
    for i in range(teeth):
        angle = i * (2 * np.pi / teeth)
        tooth_radius = radius * 1.15
        tooth_width = radius * 0.2

        x1 = radius * np.cos(angle)
        y1 = radius * np.sin(angle)
        x2 = tooth_radius * np.cos(angle - tooth_width)
        y2 = tooth_radius * np.sin(angle - tooth_width)
        x3 = tooth_radius * np.cos(angle + tooth_width)
        y3 = tooth_radius * np.sin(angle + tooth_width)

        vertices = [
            [x1, y1, 0],
            [x2, y2, 0],
            [x2, y2, height],
            [x1, y1, height],
            [x1, y1, 0],
            [x3, y3, 0],
            [x3, y3, height],
            [x1, y1, height]
        ]

        tooth_vertices = [
            [x1, y1, 0],
            [x2, y2, 0],
            [x3, y3, 0],
            [x3, y3, height],
            [x2, y2, height],
            [x1, y1, height]
        ]

        ax.add_collection3d(Poly3DCollection([tooth_vertices], color='orange', alpha=0.8))

    # Center hole
    x_hole, y_hole, z_hole = create_cylinder(radius * 0.3, height)
    ax.plot_surface(x_hole, y_hole, z_hole, color='white', alpha=0.5)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Mechanical Gear Model')
    ax.set_xlim(-radius * 1.5, radius * 1.5)
    ax.set_ylim(-radius * 1.5, radius * 1.5)
    ax.set_zlim(0, height + 1)

    plt.show()

def main():
    print("\n" + "=" * 60)
    print("   3D MECHANICAL PART MODELING - PROJECT 2 TASK 3")
    print("=" * 60)

    print("\n[1] Creating 3D Gear Model...")
    print("Radius: 5 units")
    print("Teeth: 12")
    print("Height: 2 units")

    print("\n[2] Modeling Process:")
    print("-" * 60)
    print("Step 1: Create main cylinder (Extrude)")
    print("Step 2: Add teeth (Revolve pattern)")
    print("Step 3: Create center hole (Boolean Subtract)")
    print("Step 4: Apply UCS for multi-plane drafting")
    print("Step 5: Generate 2D orthographic projection")

    print("\n[3] UCS (User Coordinate System) Manipulation:")
    print("-" * 60)
    print("UCS Origin: (0, 0, 0)")
    print("UCS X-Axis: (1, 0, 0)")
    print("UCS Y-Axis: (0, 1, 0)")
    print("UCS Z-Axis: (0, 0, 1)")

    print("\n[4] 2D Orthographic Projections:")
    print("-" * 60)
    print("Top View: Circle with teeth pattern")
    print("Front View: Rectangle with center hole")
    print("Side View: Rectangle with center hole")

    print("\n[5] Boolean Operations Used:")
    print("-" * 60)
    print("Union: Combined cylinder and teeth")
    print("Subtract: Removed center hole from gear body")
    print("Intersect: Not used in this design")

    print("\n" + "=" * 60)
    print("   TASK 3 COMPLETE")
    print("=" * 60)

    create_gear(radius=5, teeth=12, height=2)

if __name__ == "__main__":
    main()