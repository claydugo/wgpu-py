"""
All wgpu enums. Also available in the root wgpu namespace.
"""

# THIS CODE IS AUTOGENERATED - DO NOT EDIT

_use_sphinx_repr = False


class Enum:
    def __init__(self, name, **kwargs):
        self._name = name
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __iter__(self):
        return iter(
            [getattr(self, key) for key in dir(self) if not key.startswith("_")]
        )

    def __repr__(self):
        options = ", ".join(f"'{x}'" for x in self)
        if _use_sphinx_repr:  # no-cover
            return options
        return f"<{self.__class__.__name__} {self._name}: {options}>"


# There are 33 enums

PredefinedColorSpace = Enum(
    "PredefinedColorSpace",
    srgb="srgb",
)  #:

PowerPreference = Enum(
    "PowerPreference",
    low_power="low-power",
    high_performance="high-performance",
)  #:

FeatureName = Enum(
    "FeatureName",
    depth_clip_control="depth-clip-control",
    depth24unorm_stencil8="depth24unorm-stencil8",
    depth32float_stencil8="depth32float-stencil8",
    texture_compression_bc="texture-compression-bc",
    texture_compression_etc2="texture-compression-etc2",
    texture_compression_astc="texture-compression-astc",
    timestamp_query="timestamp-query",
    indirect_first_instance="indirect-first-instance",
    shader_f16="shader-f16",
)  #:

TextureDimension = Enum(
    "TextureDimension",
    d1="1d",
    d2="2d",
    d3="3d",
)  #:

TextureViewDimension = Enum(
    "TextureViewDimension",
    d1="1d",
    d2="2d",
    d2_array="2d-array",
    cube="cube",
    cube_array="cube-array",
    d3="3d",
)  #:

TextureAspect = Enum(
    "TextureAspect",
    all="all",
    stencil_only="stencil-only",
    depth_only="depth-only",
)  #:

TextureFormat = Enum(
    "TextureFormat",
    r8unorm="r8unorm",
    r8snorm="r8snorm",
    r8uint="r8uint",
    r8sint="r8sint",
    r16uint="r16uint",
    r16sint="r16sint",
    r16float="r16float",
    rg8unorm="rg8unorm",
    rg8snorm="rg8snorm",
    rg8uint="rg8uint",
    rg8sint="rg8sint",
    r32uint="r32uint",
    r32sint="r32sint",
    r32float="r32float",
    rg16uint="rg16uint",
    rg16sint="rg16sint",
    rg16float="rg16float",
    rgba8unorm="rgba8unorm",
    rgba8unorm_srgb="rgba8unorm-srgb",
    rgba8snorm="rgba8snorm",
    rgba8uint="rgba8uint",
    rgba8sint="rgba8sint",
    bgra8unorm="bgra8unorm",
    bgra8unorm_srgb="bgra8unorm-srgb",
    rgb9e5ufloat="rgb9e5ufloat",
    rgb10a2unorm="rgb10a2unorm",
    rg11b10ufloat="rg11b10ufloat",
    rg32uint="rg32uint",
    rg32sint="rg32sint",
    rg32float="rg32float",
    rgba16uint="rgba16uint",
    rgba16sint="rgba16sint",
    rgba16float="rgba16float",
    rgba32uint="rgba32uint",
    rgba32sint="rgba32sint",
    rgba32float="rgba32float",
    stencil8="stencil8",
    depth16unorm="depth16unorm",
    depth24plus="depth24plus",
    depth24plus_stencil8="depth24plus-stencil8",
    depth32float="depth32float",
    depth24unorm_stencil8="depth24unorm-stencil8",
    depth32float_stencil8="depth32float-stencil8",
    bc1_rgba_unorm="bc1-rgba-unorm",
    bc1_rgba_unorm_srgb="bc1-rgba-unorm-srgb",
    bc2_rgba_unorm="bc2-rgba-unorm",
    bc2_rgba_unorm_srgb="bc2-rgba-unorm-srgb",
    bc3_rgba_unorm="bc3-rgba-unorm",
    bc3_rgba_unorm_srgb="bc3-rgba-unorm-srgb",
    bc4_r_unorm="bc4-r-unorm",
    bc4_r_snorm="bc4-r-snorm",
    bc5_rg_unorm="bc5-rg-unorm",
    bc5_rg_snorm="bc5-rg-snorm",
    bc6h_rgb_ufloat="bc6h-rgb-ufloat",
    bc6h_rgb_float="bc6h-rgb-float",
    bc7_rgba_unorm="bc7-rgba-unorm",
    bc7_rgba_unorm_srgb="bc7-rgba-unorm-srgb",
    etc2_rgb8unorm="etc2-rgb8unorm",
    etc2_rgb8unorm_srgb="etc2-rgb8unorm-srgb",
    etc2_rgb8a1unorm="etc2-rgb8a1unorm",
    etc2_rgb8a1unorm_srgb="etc2-rgb8a1unorm-srgb",
    etc2_rgba8unorm="etc2-rgba8unorm",
    etc2_rgba8unorm_srgb="etc2-rgba8unorm-srgb",
    eac_r11unorm="eac-r11unorm",
    eac_r11snorm="eac-r11snorm",
    eac_rg11unorm="eac-rg11unorm",
    eac_rg11snorm="eac-rg11snorm",
    astc_4x4_unorm="astc-4x4-unorm",
    astc_4x4_unorm_srgb="astc-4x4-unorm-srgb",
    astc_5x4_unorm="astc-5x4-unorm",
    astc_5x4_unorm_srgb="astc-5x4-unorm-srgb",
    astc_5x5_unorm="astc-5x5-unorm",
    astc_5x5_unorm_srgb="astc-5x5-unorm-srgb",
    astc_6x5_unorm="astc-6x5-unorm",
    astc_6x5_unorm_srgb="astc-6x5-unorm-srgb",
    astc_6x6_unorm="astc-6x6-unorm",
    astc_6x6_unorm_srgb="astc-6x6-unorm-srgb",
    astc_8x5_unorm="astc-8x5-unorm",
    astc_8x5_unorm_srgb="astc-8x5-unorm-srgb",
    astc_8x6_unorm="astc-8x6-unorm",
    astc_8x6_unorm_srgb="astc-8x6-unorm-srgb",
    astc_8x8_unorm="astc-8x8-unorm",
    astc_8x8_unorm_srgb="astc-8x8-unorm-srgb",
    astc_10x5_unorm="astc-10x5-unorm",
    astc_10x5_unorm_srgb="astc-10x5-unorm-srgb",
    astc_10x6_unorm="astc-10x6-unorm",
    astc_10x6_unorm_srgb="astc-10x6-unorm-srgb",
    astc_10x8_unorm="astc-10x8-unorm",
    astc_10x8_unorm_srgb="astc-10x8-unorm-srgb",
    astc_10x10_unorm="astc-10x10-unorm",
    astc_10x10_unorm_srgb="astc-10x10-unorm-srgb",
    astc_12x10_unorm="astc-12x10-unorm",
    astc_12x10_unorm_srgb="astc-12x10-unorm-srgb",
    astc_12x12_unorm="astc-12x12-unorm",
    astc_12x12_unorm_srgb="astc-12x12-unorm-srgb",
)  #:

AddressMode = Enum(
    "AddressMode",
    clamp_to_edge="clamp-to-edge",
    repeat="repeat",
    mirror_repeat="mirror-repeat",
)  #:

FilterMode = Enum(
    "FilterMode",
    nearest="nearest",
    linear="linear",
)  #:

MipmapFilterMode = Enum(
    "MipmapFilterMode",
    nearest="nearest",
    linear="linear",
)  #:

CompareFunction = Enum(
    "CompareFunction",
    never="never",
    less="less",
    equal="equal",
    less_equal="less-equal",
    greater="greater",
    not_equal="not-equal",
    greater_equal="greater-equal",
    always="always",
)  #:

BufferBindingType = Enum(
    "BufferBindingType",
    uniform="uniform",
    storage="storage",
    read_only_storage="read-only-storage",
)  #:

SamplerBindingType = Enum(
    "SamplerBindingType",
    filtering="filtering",
    non_filtering="non-filtering",
    comparison="comparison",
)  #:

TextureSampleType = Enum(
    "TextureSampleType",
    float="float",
    unfilterable_float="unfilterable-float",
    depth="depth",
    sint="sint",
    uint="uint",
)  #:

StorageTextureAccess = Enum(
    "StorageTextureAccess",
    write_only="write-only",
)  #:

CompilationMessageType = Enum(
    "CompilationMessageType",
    error="error",
    warning="warning",
    info="info",
)  #:

PrimitiveTopology = Enum(
    "PrimitiveTopology",
    point_list="point-list",
    line_list="line-list",
    line_strip="line-strip",
    triangle_list="triangle-list",
    triangle_strip="triangle-strip",
)  #:

FrontFace = Enum(
    "FrontFace",
    ccw="ccw",
    cw="cw",
)  #:

CullMode = Enum(
    "CullMode",
    none="none",
    front="front",
    back="back",
)  #:

BlendFactor = Enum(
    "BlendFactor",
    zero="zero",
    one="one",
    src="src",
    one_minus_src="one-minus-src",
    src_alpha="src-alpha",
    one_minus_src_alpha="one-minus-src-alpha",
    dst="dst",
    one_minus_dst="one-minus-dst",
    dst_alpha="dst-alpha",
    one_minus_dst_alpha="one-minus-dst-alpha",
    src_alpha_saturated="src-alpha-saturated",
    constant="constant",
    one_minus_constant="one-minus-constant",
)  #:

BlendOperation = Enum(
    "BlendOperation",
    add="add",
    subtract="subtract",
    reverse_subtract="reverse-subtract",
    min="min",
    max="max",
)  #:

StencilOperation = Enum(
    "StencilOperation",
    keep="keep",
    zero="zero",
    replace="replace",
    invert="invert",
    increment_clamp="increment-clamp",
    decrement_clamp="decrement-clamp",
    increment_wrap="increment-wrap",
    decrement_wrap="decrement-wrap",
)  #:

IndexFormat = Enum(
    "IndexFormat",
    uint16="uint16",
    uint32="uint32",
)  #:

VertexFormat = Enum(
    "VertexFormat",
    uint8x2="uint8x2",
    uint8x4="uint8x4",
    sint8x2="sint8x2",
    sint8x4="sint8x4",
    unorm8x2="unorm8x2",
    unorm8x4="unorm8x4",
    snorm8x2="snorm8x2",
    snorm8x4="snorm8x4",
    uint16x2="uint16x2",
    uint16x4="uint16x4",
    sint16x2="sint16x2",
    sint16x4="sint16x4",
    unorm16x2="unorm16x2",
    unorm16x4="unorm16x4",
    snorm16x2="snorm16x2",
    snorm16x4="snorm16x4",
    float16x2="float16x2",
    float16x4="float16x4",
    float32="float32",
    float32x2="float32x2",
    float32x3="float32x3",
    float32x4="float32x4",
    uint32="uint32",
    uint32x2="uint32x2",
    uint32x3="uint32x3",
    uint32x4="uint32x4",
    sint32="sint32",
    sint32x2="sint32x2",
    sint32x3="sint32x3",
    sint32x4="sint32x4",
)  #:

VertexStepMode = Enum(
    "VertexStepMode",
    vertex="vertex",
    instance="instance",
)  #:

ComputePassTimestampLocation = Enum(
    "ComputePassTimestampLocation",
    beginning="beginning",
    end="end",
)  #:

RenderPassTimestampLocation = Enum(
    "RenderPassTimestampLocation",
    beginning="beginning",
    end="end",
)  #:

LoadOp = Enum(
    "LoadOp",
    load="load",
    clear="clear",
)  #:

StoreOp = Enum(
    "StoreOp",
    store="store",
    discard="discard",
)  #:

QueryType = Enum(
    "QueryType",
    occlusion="occlusion",
    timestamp="timestamp",
)  #:

CanvasCompositingAlphaMode = Enum(
    "CanvasCompositingAlphaMode",
    opaque="opaque",
    premultiplied="premultiplied",
)  #:

DeviceLostReason = Enum(
    "DeviceLostReason",
    destroyed="destroyed",
)  #:

ErrorFilter = Enum(
    "ErrorFilter",
    out_of_memory="out-of-memory",
    validation="validation",
)  #:
