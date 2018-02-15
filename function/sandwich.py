def make_sandwich(*components):
    """Выводит список компонентов сэндвича."""
    print("\nMaking a sandwich with the following components:")
    for component in components:
        print("- " + component)

make_sandwich('cheese')
make_sandwich('tomatos', 'cucumber', 'salad')
make_sandwich('fish', 'potato')
