# Dassault Systèmes Enterprise PBR Shading Model (DSPBR) 2021x extensions

## Overview

This set of extensions defines the Dassault Systèmes Enterprise PBR Shading Model (DSPBR) 2021x for glTF.

* The [Specification](https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec-2021x.md.html) 
* The [User Guide](https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/user_guide.md.html) 

The Dassault Systèmes Enterprise PBR material is defined by adding the respective `3DS_` extension(s) to any glTF material. The extensions reuse the `pbrMetallicRoughness` parameters for parameterization of a new energy conserving microfacet roughness model.

### `pbrMetallicRoughness` Parameter Mappings

```
baseColorFactor.xyz -> albedo
metallicFactor -> metallic
roughnessFactor -> roughness
alphaMode set to "BLEND" + baseColor.w -> cutoutOpacity
emissiveFactor -> emissionColor * emissionValue
```

```json
{
    "materials": [
          {
            "name": "Gold",
            "pbrMetallicRoughness": {
                "baseColorFactor": [ 1.000, 0.766, 0.336, 1.0 ],
                "metallicFactor": 1.0,
                "roughnessFactor": 0.0
            }
        }
    ]
}
```

## Examples

```json
{
    "name": "Leather",
    "normalTexture": {
        "index": 2,
        "texCoord": 0
    },
    "pbrMetallicRoughness": {
        "baseColorTexture": {
            "index": 0,
            "texCoord": 0
        },
        "metallicRoughnessTexture": {
            "index": 1,
            "texCoord": 0
        }
    },
    "extensions": {
        "KHR_materials_clearcoat": {
            "clearcoatFactor": 0.0,
            "clearcoatRoughnessFactor": 0.0,
        },
        "3DS_materials_anisotropy": {
            "anisotropyFactor": 0.0,
            "anisotropyRotationFactor": 0.0
        },
        "3DS_materials_transparency": {
            "transparencyFactor": 0.0
        },
        "3DS_materials_translucency": {
            "translucencyFactor": 0.0
        },
        "3DS_materials_sheen": {
            "sheenFactor": 0.0,
            "sheenColorFactor": [ 1.0, 1.0, 1.0 ],
            "sheenRoughnessFactor": 0.2
        },
        "3DS_materials_specular": {
            "specularFactor": 1.0,
            "specularColorFactor": [ 1.0, 1.0, 1.0 ]
        },
        "3DS_materials_ior": {
            "ior": 1.5
        },
        "3DS_materials_volume": {
            "thinWalled": false,
            "attenuationColor": [ 1.0, 1.0, 1.0 ],
            "attenuationDistance": 200.0,
            "subsurfaceColor": [ 0.0, 0.0, 0.0 ]
        }
    }
}
```

```json
{
    "name": "Light",
    "emissiveFactor": [
        0.8882734775543213,
        0.46548381447792055,
        0.11881855130195618
    ],
    "pbrMetallicRoughness": {
        "baseColorFactor": [
            0.935836672782898,
            0.7405970096588135,
            0.7048523426055908,
            1.0
        ],
        "roughnessFactor": 0.0,
        "metallicFactor": 0.0
    },
    "extensions": {
        "3DS_materials_emission": {
            "emissionMode": "POWER",
            "emissionEnergyNormalization": false
        }
    }
}
```
