from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")


results = model("cardPics/test002.jpg", save=True)

for result in results:
    annotated = result.plot(
        conf=True,
        labels=True,
        boxes=True,
        line_width=2,
        font_size=0.5
    )

print(results)
print(type(results))


for result in results:
    for box in result.boxes:
        classID = int(box.cls.item())
        confidence = float(box.conf.item())
        cardName = result.names[classID]

        print(f"{cardName}: {confidence:.2%}")




# if __name__ == "__main__":
#     model.train(resume=True)


# if __name__ == "__main__":
#     results = model.train(  
#         data="dataset/data.yaml",
#         epochs=50,
#         imgsz=640,
#         device=0
#     )