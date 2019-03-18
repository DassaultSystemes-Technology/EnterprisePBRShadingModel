# 3DS_materials_enterprise_pbr

## Status

Draft 

## Dependencies

Written against the glTF 2.0 spec.

## Overview

This extension defines the Dassault Systèmes Enterprise PBR Shading Model (DSPBR) for glTF. 

* The [Specification](https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec.md.html) 
* The [User Guide](https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/user_guide.md.html) 

## Extending Materials

The Dassault Systèmes Enterprise PBR material is defined by adding the `3DS_materials_enterprise_pbr` extension to any glTF material. 
The extension reuses the `pbrMetallicRoughness` parameters for parameterization of a new energy conserving microfacet roughness model. It further introduces additional parameters for new effects as defined by the [Specification](https://dassaultsystemes-technology.github.io/EnterprisePBRShadingModel/spec.md.html). 

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
            },
            "extensions": {
                "3DS_materials_enterprise_pbr": {}
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
        "3DS_materials_enterprise_pbr": {
            "anisotropy": 0.0,
            "anisotropyRotation": 0.0,
            "transparency": 0.0,
            "sheen": 0.0,
            "specular": 1.0,
            "specularTint": [
                1.0,
                1.0,
                1.0
            ],
            "clearcoat": 0.0,
            "clearcoatRoughness": 0.0,
            "ior": 1.5,
            "thinWalled": true,
            "attenuationColor": [
                1.0,
                1.0,
                1.0
            ],
            "attenuationDistance": 100000.0,
            "subsurfaceColor": [
                0.0,
                0.0,
                0.0
            ]
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
        "3DS_materials_enterprise_pbr": {
            "anisotropy": 0.0,
            "anisotropyRotation": 0.0,
            "transparency": 0.0,
            "sheen": 0.0,
            "specular": 0.0,
            "specularTint": [
                0.0,
                0.0,
                0.0
            ],
            "clearcoat": 0.0,
            "clearcoatRoughness": 0.0,
            "ior": 1.5,
            "thinWalled": true,          
            "emissionMode": "POWER"
        }
    }
}    
```
