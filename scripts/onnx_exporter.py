import torch
import torchvision.models as models
import argparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--save", default="model.onnx")
    args = parser.parse_args()


    print(">>>>> Download Pretrained Resnet50 Start ...")
    resnet50 = models.resnet50(pretrained=True)
    print(">>>>> Download Pretrained Resnet50 End")

    dummy_input = torch.randn(1, 3, 224, 224)

    print(">>>>> Convert Pretrained Resnet50 to Inference Mode Start ...")
    resnet50 = resnet50.eval()
    print(">>>>> Convert Pretrained Resnet50 to Inference Mode End")

    print(">>>>> Convert Pretrained Resnet50 to ONNX format Start ...")
    torch.onnx.export(
        resnet50,
        dummy_input,
        args.save,
        export_params=True,
        opset_version=11,
        do_constant_folding=True,
        input_names=["input"],
        output_names=["output"],
        dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}},
    )
    print(">>>>> Convert Pretrained Resnet50 to ONNX format End")

    print("Saved {}".format(args.save))
	
