from image_resize import Img_Resize


def main():
    Img_Resize('Books_Before_Resize', 'books', 'book')
    Img_Resize('Shoes_Before_Resize', 'shoes', 'shoe')
    Img_Resize('Chairs_Before_Resize', 'chairs', 'chair')
    Img_Resize('Fridges_Before_Resize', 'fridges', 'fridge')
    Img_Resize('Tables_Before_Resize', 'tables', 'table')
    print("done")

if __name__ == "__main__":
    main()
