# Code generated from constants.py; DO NOT EDIT MANUALLY.
#
# To regenerate, run: python tools/gen_code_table.py
#
# These constants provide type-safe Code values for all known multicodecs,
# allowing usage like:
#     from multicodec import SHA2_256
#     code = SHA2_256  # Code object for sha2-256
#
# Instead of:
#     from multicodec import Code
#     code = Code(0x12)

from __future__ import annotations

from .code import Code

# Multihash
IDENTITY: Code = Code(0x00)  # identity
SHA1: Code = Code(0x11)  # sha1
SHA2_256: Code = Code(0x12)  # sha2-256
SHA2_512: Code = Code(0x13)  # sha2-512
SHA3_512: Code = Code(0x14)  # sha3-512
SHA3_384: Code = Code(0x15)  # sha3-384
SHA3_256: Code = Code(0x16)  # sha3-256
SHA3_224: Code = Code(0x17)  # sha3-224
SHAKE_128: Code = Code(0x18)  # shake-128
SHAKE_256: Code = Code(0x19)  # shake-256
KECCAK_224: Code = Code(0x1A)  # keccak-224
KECCAK_256: Code = Code(0x1B)  # keccak-256
KECCAK_384: Code = Code(0x1C)  # keccak-384
KECCAK_512: Code = Code(0x1D)  # keccak-512
BLAKE3: Code = Code(0x1E)  # blake3
SHA2_384: Code = Code(0x20)  # sha2-384
MURMUR3_X64_64: Code = Code(0x22)  # murmur3-x64-64
MURMUR3_32: Code = Code(0x23)  # murmur3-32
DBL_SHA2_256: Code = Code(0x56)  # dbl-sha2-256
BLAKE3_HASHSEQ: Code = Code(0x80)  # blake3-hashseq
MD4: Code = Code(0xD4)  # md4
MD5: Code = Code(0xD5)  # md5
FR32_SHA256_TRUNC254_PADBINTREE: Code = Code(0x1011)  # fr32-sha256-trunc254-padbintree
SHA2_256_TRUNC254_PADDED: Code = Code(0x1012)  # sha2-256-trunc254-padded
SHA2_224: Code = Code(0x1013)  # sha2-224
SHA2_512_224: Code = Code(0x1014)  # sha2-512-224
SHA2_512_256: Code = Code(0x1015)  # sha2-512-256
MURMUR3_X64_128: Code = Code(0x1022)  # murmur3-x64-128
RIPEMD_128: Code = Code(0x1052)  # ripemd-128
RIPEMD_160: Code = Code(0x1053)  # ripemd-160
RIPEMD_256: Code = Code(0x1054)  # ripemd-256
RIPEMD_320: Code = Code(0x1055)  # ripemd-320
X11: Code = Code(0x1100)  # x11
BLS12_381_G1_PUB_SHARE: Code = Code(0x130C)  # bls12_381-g1-pub-share
BLS12_381_G2_PUB_SHARE: Code = Code(0x130D)  # bls12_381-g2-pub-share
BLS12_381_G1_PRIV_SHARE: Code = Code(0x130E)  # bls12_381-g1-priv-share
BLS12_381_G2_PRIV_SHARE: Code = Code(0x130F)  # bls12_381-g2-priv-share
LAMPORT_SHA3_512_PUB: Code = Code(0x1A14)  # lamport-sha3-512-pub
LAMPORT_SHA3_384_PUB: Code = Code(0x1A15)  # lamport-sha3-384-pub
LAMPORT_SHA3_256_PUB: Code = Code(0x1A16)  # lamport-sha3-256-pub
LAMPORT_SHA3_512_PRIV: Code = Code(0x1A24)  # lamport-sha3-512-priv
LAMPORT_SHA3_384_PRIV: Code = Code(0x1A25)  # lamport-sha3-384-priv
LAMPORT_SHA3_256_PRIV: Code = Code(0x1A26)  # lamport-sha3-256-priv
LAMPORT_SHA3_512_PRIV_SHARE: Code = Code(0x1A34)  # lamport-sha3-512-priv-share
LAMPORT_SHA3_384_PRIV_SHARE: Code = Code(0x1A35)  # lamport-sha3-384-priv-share
LAMPORT_SHA3_256_PRIV_SHARE: Code = Code(0x1A36)  # lamport-sha3-256-priv-share
LAMPORT_SHA3_512_SIG: Code = Code(0x1A44)  # lamport-sha3-512-sig
LAMPORT_SHA3_384_SIG: Code = Code(0x1A45)  # lamport-sha3-384-sig
LAMPORT_SHA3_256_SIG: Code = Code(0x1A46)  # lamport-sha3-256-sig
LAMPORT_SHA3_512_SIG_SHARE: Code = Code(0x1A54)  # lamport-sha3-512-sig-share
LAMPORT_SHA3_384_SIG_SHARE: Code = Code(0x1A55)  # lamport-sha3-384-sig-share
LAMPORT_SHA3_256_SIG_SHARE: Code = Code(0x1A56)  # lamport-sha3-256-sig-share
KANGAROOTWELVE: Code = Code(0x1D01)  # kangarootwelve
SM3_256: Code = Code(0x534D)  # sm3-256
SHA256A: Code = Code(0x7012)  # sha256a
BLAKE2B_8: Code = Code(0xB201)  # blake2b-8
BLAKE2B_16: Code = Code(0xB202)  # blake2b-16
BLAKE2B_24: Code = Code(0xB203)  # blake2b-24
BLAKE2B_32: Code = Code(0xB204)  # blake2b-32
BLAKE2B_40: Code = Code(0xB205)  # blake2b-40
BLAKE2B_48: Code = Code(0xB206)  # blake2b-48
BLAKE2B_56: Code = Code(0xB207)  # blake2b-56
BLAKE2B_64: Code = Code(0xB208)  # blake2b-64
BLAKE2B_72: Code = Code(0xB209)  # blake2b-72
BLAKE2B_80: Code = Code(0xB20A)  # blake2b-80
BLAKE2B_88: Code = Code(0xB20B)  # blake2b-88
BLAKE2B_96: Code = Code(0xB20C)  # blake2b-96
BLAKE2B_104: Code = Code(0xB20D)  # blake2b-104
BLAKE2B_112: Code = Code(0xB20E)  # blake2b-112
BLAKE2B_120: Code = Code(0xB20F)  # blake2b-120
BLAKE2B_128: Code = Code(0xB210)  # blake2b-128
BLAKE2B_136: Code = Code(0xB211)  # blake2b-136
BLAKE2B_144: Code = Code(0xB212)  # blake2b-144
BLAKE2B_152: Code = Code(0xB213)  # blake2b-152
BLAKE2B_160: Code = Code(0xB214)  # blake2b-160
BLAKE2B_168: Code = Code(0xB215)  # blake2b-168
BLAKE2B_176: Code = Code(0xB216)  # blake2b-176
BLAKE2B_184: Code = Code(0xB217)  # blake2b-184
BLAKE2B_192: Code = Code(0xB218)  # blake2b-192
BLAKE2B_200: Code = Code(0xB219)  # blake2b-200
BLAKE2B_208: Code = Code(0xB21A)  # blake2b-208
BLAKE2B_216: Code = Code(0xB21B)  # blake2b-216
BLAKE2B_224: Code = Code(0xB21C)  # blake2b-224
BLAKE2B_232: Code = Code(0xB21D)  # blake2b-232
BLAKE2B_240: Code = Code(0xB21E)  # blake2b-240
BLAKE2B_248: Code = Code(0xB21F)  # blake2b-248
BLAKE2B_256: Code = Code(0xB220)  # blake2b-256
BLAKE2B_264: Code = Code(0xB221)  # blake2b-264
BLAKE2B_272: Code = Code(0xB222)  # blake2b-272
BLAKE2B_280: Code = Code(0xB223)  # blake2b-280
BLAKE2B_288: Code = Code(0xB224)  # blake2b-288
BLAKE2B_296: Code = Code(0xB225)  # blake2b-296
BLAKE2B_304: Code = Code(0xB226)  # blake2b-304
BLAKE2B_312: Code = Code(0xB227)  # blake2b-312
BLAKE2B_320: Code = Code(0xB228)  # blake2b-320
BLAKE2B_328: Code = Code(0xB229)  # blake2b-328
BLAKE2B_336: Code = Code(0xB22A)  # blake2b-336
BLAKE2B_344: Code = Code(0xB22B)  # blake2b-344
BLAKE2B_352: Code = Code(0xB22C)  # blake2b-352
BLAKE2B_360: Code = Code(0xB22D)  # blake2b-360
BLAKE2B_368: Code = Code(0xB22E)  # blake2b-368
BLAKE2B_376: Code = Code(0xB22F)  # blake2b-376
BLAKE2B_384: Code = Code(0xB230)  # blake2b-384
BLAKE2B_392: Code = Code(0xB231)  # blake2b-392
BLAKE2B_400: Code = Code(0xB232)  # blake2b-400
BLAKE2B_408: Code = Code(0xB233)  # blake2b-408
BLAKE2B_416: Code = Code(0xB234)  # blake2b-416
BLAKE2B_424: Code = Code(0xB235)  # blake2b-424
BLAKE2B_432: Code = Code(0xB236)  # blake2b-432
BLAKE2B_440: Code = Code(0xB237)  # blake2b-440
BLAKE2B_448: Code = Code(0xB238)  # blake2b-448
BLAKE2B_456: Code = Code(0xB239)  # blake2b-456
BLAKE2B_464: Code = Code(0xB23A)  # blake2b-464
BLAKE2B_472: Code = Code(0xB23B)  # blake2b-472
BLAKE2B_480: Code = Code(0xB23C)  # blake2b-480
BLAKE2B_488: Code = Code(0xB23D)  # blake2b-488
BLAKE2B_496: Code = Code(0xB23E)  # blake2b-496
BLAKE2B_504: Code = Code(0xB23F)  # blake2b-504
BLAKE2B_512: Code = Code(0xB240)  # blake2b-512
BLAKE2S_8: Code = Code(0xB241)  # blake2s-8
BLAKE2S_16: Code = Code(0xB242)  # blake2s-16
BLAKE2S_24: Code = Code(0xB243)  # blake2s-24
BLAKE2S_32: Code = Code(0xB244)  # blake2s-32
BLAKE2S_40: Code = Code(0xB245)  # blake2s-40
BLAKE2S_48: Code = Code(0xB246)  # blake2s-48
BLAKE2S_56: Code = Code(0xB247)  # blake2s-56
BLAKE2S_64: Code = Code(0xB248)  # blake2s-64
BLAKE2S_72: Code = Code(0xB249)  # blake2s-72
BLAKE2S_80: Code = Code(0xB24A)  # blake2s-80
BLAKE2S_88: Code = Code(0xB24B)  # blake2s-88
BLAKE2S_96: Code = Code(0xB24C)  # blake2s-96
BLAKE2S_104: Code = Code(0xB24D)  # blake2s-104
BLAKE2S_112: Code = Code(0xB24E)  # blake2s-112
BLAKE2S_120: Code = Code(0xB24F)  # blake2s-120
BLAKE2S_128: Code = Code(0xB250)  # blake2s-128
BLAKE2S_136: Code = Code(0xB251)  # blake2s-136
BLAKE2S_144: Code = Code(0xB252)  # blake2s-144
BLAKE2S_152: Code = Code(0xB253)  # blake2s-152
BLAKE2S_160: Code = Code(0xB254)  # blake2s-160
BLAKE2S_168: Code = Code(0xB255)  # blake2s-168
BLAKE2S_176: Code = Code(0xB256)  # blake2s-176
BLAKE2S_184: Code = Code(0xB257)  # blake2s-184
BLAKE2S_192: Code = Code(0xB258)  # blake2s-192
BLAKE2S_200: Code = Code(0xB259)  # blake2s-200
BLAKE2S_208: Code = Code(0xB25A)  # blake2s-208
BLAKE2S_216: Code = Code(0xB25B)  # blake2s-216
BLAKE2S_224: Code = Code(0xB25C)  # blake2s-224
BLAKE2S_232: Code = Code(0xB25D)  # blake2s-232
BLAKE2S_240: Code = Code(0xB25E)  # blake2s-240
BLAKE2S_248: Code = Code(0xB25F)  # blake2s-248
BLAKE2S_256: Code = Code(0xB260)  # blake2s-256
SKEIN256_8: Code = Code(0xB301)  # skein256-8
SKEIN256_16: Code = Code(0xB302)  # skein256-16
SKEIN256_24: Code = Code(0xB303)  # skein256-24
SKEIN256_32: Code = Code(0xB304)  # skein256-32
SKEIN256_40: Code = Code(0xB305)  # skein256-40
SKEIN256_48: Code = Code(0xB306)  # skein256-48
SKEIN256_56: Code = Code(0xB307)  # skein256-56
SKEIN256_64: Code = Code(0xB308)  # skein256-64
SKEIN256_72: Code = Code(0xB309)  # skein256-72
SKEIN256_80: Code = Code(0xB30A)  # skein256-80
SKEIN256_88: Code = Code(0xB30B)  # skein256-88
SKEIN256_96: Code = Code(0xB30C)  # skein256-96
SKEIN256_104: Code = Code(0xB30D)  # skein256-104
SKEIN256_112: Code = Code(0xB30E)  # skein256-112
SKEIN256_120: Code = Code(0xB30F)  # skein256-120
SKEIN256_128: Code = Code(0xB310)  # skein256-128
SKEIN256_136: Code = Code(0xB311)  # skein256-136
SKEIN256_144: Code = Code(0xB312)  # skein256-144
SKEIN256_152: Code = Code(0xB313)  # skein256-152
SKEIN256_160: Code = Code(0xB314)  # skein256-160
SKEIN256_168: Code = Code(0xB315)  # skein256-168
SKEIN256_176: Code = Code(0xB316)  # skein256-176
SKEIN256_184: Code = Code(0xB317)  # skein256-184
SKEIN256_192: Code = Code(0xB318)  # skein256-192
SKEIN256_200: Code = Code(0xB319)  # skein256-200
SKEIN256_208: Code = Code(0xB31A)  # skein256-208
SKEIN256_216: Code = Code(0xB31B)  # skein256-216
SKEIN256_224: Code = Code(0xB31C)  # skein256-224
SKEIN256_232: Code = Code(0xB31D)  # skein256-232
SKEIN256_240: Code = Code(0xB31E)  # skein256-240
SKEIN256_248: Code = Code(0xB31F)  # skein256-248
SKEIN256_256: Code = Code(0xB320)  # skein256-256
SKEIN512_8: Code = Code(0xB321)  # skein512-8
SKEIN512_16: Code = Code(0xB322)  # skein512-16
SKEIN512_24: Code = Code(0xB323)  # skein512-24
SKEIN512_32: Code = Code(0xB324)  # skein512-32
SKEIN512_40: Code = Code(0xB325)  # skein512-40
SKEIN512_48: Code = Code(0xB326)  # skein512-48
SKEIN512_56: Code = Code(0xB327)  # skein512-56
SKEIN512_64: Code = Code(0xB328)  # skein512-64
SKEIN512_72: Code = Code(0xB329)  # skein512-72
SKEIN512_80: Code = Code(0xB32A)  # skein512-80
SKEIN512_88: Code = Code(0xB32B)  # skein512-88
SKEIN512_96: Code = Code(0xB32C)  # skein512-96
SKEIN512_104: Code = Code(0xB32D)  # skein512-104
SKEIN512_112: Code = Code(0xB32E)  # skein512-112
SKEIN512_120: Code = Code(0xB32F)  # skein512-120
SKEIN512_128: Code = Code(0xB330)  # skein512-128
SKEIN512_136: Code = Code(0xB331)  # skein512-136
SKEIN512_144: Code = Code(0xB332)  # skein512-144
SKEIN512_152: Code = Code(0xB333)  # skein512-152
SKEIN512_160: Code = Code(0xB334)  # skein512-160
SKEIN512_168: Code = Code(0xB335)  # skein512-168
SKEIN512_176: Code = Code(0xB336)  # skein512-176
SKEIN512_184: Code = Code(0xB337)  # skein512-184
SKEIN512_192: Code = Code(0xB338)  # skein512-192
SKEIN512_200: Code = Code(0xB339)  # skein512-200
SKEIN512_208: Code = Code(0xB33A)  # skein512-208
SKEIN512_216: Code = Code(0xB33B)  # skein512-216
SKEIN512_224: Code = Code(0xB33C)  # skein512-224
SKEIN512_232: Code = Code(0xB33D)  # skein512-232
SKEIN512_240: Code = Code(0xB33E)  # skein512-240
SKEIN512_248: Code = Code(0xB33F)  # skein512-248
SKEIN512_256: Code = Code(0xB340)  # skein512-256
SKEIN512_264: Code = Code(0xB341)  # skein512-264
SKEIN512_272: Code = Code(0xB342)  # skein512-272
SKEIN512_280: Code = Code(0xB343)  # skein512-280
SKEIN512_288: Code = Code(0xB344)  # skein512-288
SKEIN512_296: Code = Code(0xB345)  # skein512-296
SKEIN512_304: Code = Code(0xB346)  # skein512-304
SKEIN512_312: Code = Code(0xB347)  # skein512-312
SKEIN512_320: Code = Code(0xB348)  # skein512-320
SKEIN512_328: Code = Code(0xB349)  # skein512-328
SKEIN512_336: Code = Code(0xB34A)  # skein512-336
SKEIN512_344: Code = Code(0xB34B)  # skein512-344
SKEIN512_352: Code = Code(0xB34C)  # skein512-352
SKEIN512_360: Code = Code(0xB34D)  # skein512-360
SKEIN512_368: Code = Code(0xB34E)  # skein512-368
SKEIN512_376: Code = Code(0xB34F)  # skein512-376
SKEIN512_384: Code = Code(0xB350)  # skein512-384
SKEIN512_392: Code = Code(0xB351)  # skein512-392
SKEIN512_400: Code = Code(0xB352)  # skein512-400
SKEIN512_408: Code = Code(0xB353)  # skein512-408
SKEIN512_416: Code = Code(0xB354)  # skein512-416
SKEIN512_424: Code = Code(0xB355)  # skein512-424
SKEIN512_432: Code = Code(0xB356)  # skein512-432
SKEIN512_440: Code = Code(0xB357)  # skein512-440
SKEIN512_448: Code = Code(0xB358)  # skein512-448
SKEIN512_456: Code = Code(0xB359)  # skein512-456
SKEIN512_464: Code = Code(0xB35A)  # skein512-464
SKEIN512_472: Code = Code(0xB35B)  # skein512-472
SKEIN512_480: Code = Code(0xB35C)  # skein512-480
SKEIN512_488: Code = Code(0xB35D)  # skein512-488
SKEIN512_496: Code = Code(0xB35E)  # skein512-496
SKEIN512_504: Code = Code(0xB35F)  # skein512-504
SKEIN512_512: Code = Code(0xB360)  # skein512-512
SKEIN1024_8: Code = Code(0xB361)  # skein1024-8
SKEIN1024_16: Code = Code(0xB362)  # skein1024-16
SKEIN1024_24: Code = Code(0xB363)  # skein1024-24
SKEIN1024_32: Code = Code(0xB364)  # skein1024-32
SKEIN1024_40: Code = Code(0xB365)  # skein1024-40
SKEIN1024_48: Code = Code(0xB366)  # skein1024-48
SKEIN1024_56: Code = Code(0xB367)  # skein1024-56
SKEIN1024_64: Code = Code(0xB368)  # skein1024-64
SKEIN1024_72: Code = Code(0xB369)  # skein1024-72
SKEIN1024_80: Code = Code(0xB36A)  # skein1024-80
SKEIN1024_88: Code = Code(0xB36B)  # skein1024-88
SKEIN1024_96: Code = Code(0xB36C)  # skein1024-96
SKEIN1024_104: Code = Code(0xB36D)  # skein1024-104
SKEIN1024_112: Code = Code(0xB36E)  # skein1024-112
SKEIN1024_120: Code = Code(0xB36F)  # skein1024-120
SKEIN1024_128: Code = Code(0xB370)  # skein1024-128
SKEIN1024_136: Code = Code(0xB371)  # skein1024-136
SKEIN1024_144: Code = Code(0xB372)  # skein1024-144
SKEIN1024_152: Code = Code(0xB373)  # skein1024-152
SKEIN1024_160: Code = Code(0xB374)  # skein1024-160
SKEIN1024_168: Code = Code(0xB375)  # skein1024-168
SKEIN1024_176: Code = Code(0xB376)  # skein1024-176
SKEIN1024_184: Code = Code(0xB377)  # skein1024-184
SKEIN1024_192: Code = Code(0xB378)  # skein1024-192
SKEIN1024_200: Code = Code(0xB379)  # skein1024-200
SKEIN1024_208: Code = Code(0xB37A)  # skein1024-208
SKEIN1024_216: Code = Code(0xB37B)  # skein1024-216
SKEIN1024_224: Code = Code(0xB37C)  # skein1024-224
SKEIN1024_232: Code = Code(0xB37D)  # skein1024-232
SKEIN1024_240: Code = Code(0xB37E)  # skein1024-240
SKEIN1024_248: Code = Code(0xB37F)  # skein1024-248
SKEIN1024_256: Code = Code(0xB380)  # skein1024-256
SKEIN1024_264: Code = Code(0xB381)  # skein1024-264
SKEIN1024_272: Code = Code(0xB382)  # skein1024-272
SKEIN1024_280: Code = Code(0xB383)  # skein1024-280
SKEIN1024_288: Code = Code(0xB384)  # skein1024-288
SKEIN1024_296: Code = Code(0xB385)  # skein1024-296
SKEIN1024_304: Code = Code(0xB386)  # skein1024-304
SKEIN1024_312: Code = Code(0xB387)  # skein1024-312
SKEIN1024_320: Code = Code(0xB388)  # skein1024-320
SKEIN1024_328: Code = Code(0xB389)  # skein1024-328
SKEIN1024_336: Code = Code(0xB38A)  # skein1024-336
SKEIN1024_344: Code = Code(0xB38B)  # skein1024-344
SKEIN1024_352: Code = Code(0xB38C)  # skein1024-352
SKEIN1024_360: Code = Code(0xB38D)  # skein1024-360
SKEIN1024_368: Code = Code(0xB38E)  # skein1024-368
SKEIN1024_376: Code = Code(0xB38F)  # skein1024-376
SKEIN1024_384: Code = Code(0xB390)  # skein1024-384
SKEIN1024_392: Code = Code(0xB391)  # skein1024-392
SKEIN1024_400: Code = Code(0xB392)  # skein1024-400
SKEIN1024_408: Code = Code(0xB393)  # skein1024-408
SKEIN1024_416: Code = Code(0xB394)  # skein1024-416
SKEIN1024_424: Code = Code(0xB395)  # skein1024-424
SKEIN1024_432: Code = Code(0xB396)  # skein1024-432
SKEIN1024_440: Code = Code(0xB397)  # skein1024-440
SKEIN1024_448: Code = Code(0xB398)  # skein1024-448
SKEIN1024_456: Code = Code(0xB399)  # skein1024-456
SKEIN1024_464: Code = Code(0xB39A)  # skein1024-464
SKEIN1024_472: Code = Code(0xB39B)  # skein1024-472
SKEIN1024_480: Code = Code(0xB39C)  # skein1024-480
SKEIN1024_488: Code = Code(0xB39D)  # skein1024-488
SKEIN1024_496: Code = Code(0xB39E)  # skein1024-496
SKEIN1024_504: Code = Code(0xB39F)  # skein1024-504
SKEIN1024_512: Code = Code(0xB3A0)  # skein1024-512
SKEIN1024_520: Code = Code(0xB3A1)  # skein1024-520
SKEIN1024_528: Code = Code(0xB3A2)  # skein1024-528
SKEIN1024_536: Code = Code(0xB3A3)  # skein1024-536
SKEIN1024_544: Code = Code(0xB3A4)  # skein1024-544
SKEIN1024_552: Code = Code(0xB3A5)  # skein1024-552
SKEIN1024_560: Code = Code(0xB3A6)  # skein1024-560
SKEIN1024_568: Code = Code(0xB3A7)  # skein1024-568
SKEIN1024_576: Code = Code(0xB3A8)  # skein1024-576
SKEIN1024_584: Code = Code(0xB3A9)  # skein1024-584
SKEIN1024_592: Code = Code(0xB3AA)  # skein1024-592
SKEIN1024_600: Code = Code(0xB3AB)  # skein1024-600
SKEIN1024_608: Code = Code(0xB3AC)  # skein1024-608
SKEIN1024_616: Code = Code(0xB3AD)  # skein1024-616
SKEIN1024_624: Code = Code(0xB3AE)  # skein1024-624
SKEIN1024_632: Code = Code(0xB3AF)  # skein1024-632
SKEIN1024_640: Code = Code(0xB3B0)  # skein1024-640
SKEIN1024_648: Code = Code(0xB3B1)  # skein1024-648
SKEIN1024_656: Code = Code(0xB3B2)  # skein1024-656
SKEIN1024_664: Code = Code(0xB3B3)  # skein1024-664
SKEIN1024_672: Code = Code(0xB3B4)  # skein1024-672
SKEIN1024_680: Code = Code(0xB3B5)  # skein1024-680
SKEIN1024_688: Code = Code(0xB3B6)  # skein1024-688
SKEIN1024_696: Code = Code(0xB3B7)  # skein1024-696
SKEIN1024_704: Code = Code(0xB3B8)  # skein1024-704
SKEIN1024_712: Code = Code(0xB3B9)  # skein1024-712
SKEIN1024_720: Code = Code(0xB3BA)  # skein1024-720
SKEIN1024_728: Code = Code(0xB3BB)  # skein1024-728
SKEIN1024_736: Code = Code(0xB3BC)  # skein1024-736
SKEIN1024_744: Code = Code(0xB3BD)  # skein1024-744
SKEIN1024_752: Code = Code(0xB3BE)  # skein1024-752
SKEIN1024_760: Code = Code(0xB3BF)  # skein1024-760
SKEIN1024_768: Code = Code(0xB3C0)  # skein1024-768
SKEIN1024_776: Code = Code(0xB3C1)  # skein1024-776
SKEIN1024_784: Code = Code(0xB3C2)  # skein1024-784
SKEIN1024_792: Code = Code(0xB3C3)  # skein1024-792
SKEIN1024_800: Code = Code(0xB3C4)  # skein1024-800
SKEIN1024_808: Code = Code(0xB3C5)  # skein1024-808
SKEIN1024_816: Code = Code(0xB3C6)  # skein1024-816
SKEIN1024_824: Code = Code(0xB3C7)  # skein1024-824
SKEIN1024_832: Code = Code(0xB3C8)  # skein1024-832
SKEIN1024_840: Code = Code(0xB3C9)  # skein1024-840
SKEIN1024_848: Code = Code(0xB3CA)  # skein1024-848
SKEIN1024_856: Code = Code(0xB3CB)  # skein1024-856
SKEIN1024_864: Code = Code(0xB3CC)  # skein1024-864
SKEIN1024_872: Code = Code(0xB3CD)  # skein1024-872
SKEIN1024_880: Code = Code(0xB3CE)  # skein1024-880
SKEIN1024_888: Code = Code(0xB3CF)  # skein1024-888
SKEIN1024_896: Code = Code(0xB3D0)  # skein1024-896
SKEIN1024_904: Code = Code(0xB3D1)  # skein1024-904
SKEIN1024_912: Code = Code(0xB3D2)  # skein1024-912
SKEIN1024_920: Code = Code(0xB3D3)  # skein1024-920
SKEIN1024_928: Code = Code(0xB3D4)  # skein1024-928
SKEIN1024_936: Code = Code(0xB3D5)  # skein1024-936
SKEIN1024_944: Code = Code(0xB3D6)  # skein1024-944
SKEIN1024_952: Code = Code(0xB3D7)  # skein1024-952
SKEIN1024_960: Code = Code(0xB3D8)  # skein1024-960
SKEIN1024_968: Code = Code(0xB3D9)  # skein1024-968
SKEIN1024_976: Code = Code(0xB3DA)  # skein1024-976
SKEIN1024_984: Code = Code(0xB3DB)  # skein1024-984
SKEIN1024_992: Code = Code(0xB3DC)  # skein1024-992
SKEIN1024_1000: Code = Code(0xB3DD)  # skein1024-1000
SKEIN1024_1008: Code = Code(0xB3DE)  # skein1024-1008
SKEIN1024_1016: Code = Code(0xB3DF)  # skein1024-1016
SKEIN1024_1024: Code = Code(0xB3E0)  # skein1024-1024
POSEIDON_BLS12_381_A2_FC1: Code = Code(0xB401)  # poseidon-bls12_381-a2-fc1
POSEIDON_BLS12_381_A2_FC1_SC: Code = Code(0xB402)  # poseidon-bls12_381-a2-fc1-sc
SSZ_SHA2_256_BMT: Code = Code(0xB502)  # ssz-sha2-256-bmt
SHA2_256_CHUNKED: Code = Code(0xB510)  # sha2-256-chunked
BLS12_381_G1_SHARE_MSIG: Code = Code(0xD01304)  # bls12_381-g1-share-msig
BLS12_381_G2_SHARE_MSIG: Code = Code(0xD01305)  # bls12_381-g2-share-msig
LAMPORT_SHARE_MSIG: Code = Code(0xD01307)  # lamport-share-msig

# Multiaddr
IP4: Code = Code(0x04)  # ip4
TCP: Code = Code(0x06)  # tcp
DCCP: Code = Code(0x21)  # dccp
IP6: Code = Code(0x29)  # ip6
IP6ZONE: Code = Code(0x2A)  # ip6zone
DNS: Code = Code(0x35)  # dns
DNS4: Code = Code(0x36)  # dns4
DNS6: Code = Code(0x37)  # dns6
DNSADDR: Code = Code(0x38)  # dnsaddr
LIBP2P_KEY: Code = Code(0x72)  # libp2p-key
SCTP: Code = Code(0x84)  # sctp
DNSLINK: Code = Code(0xE8)  # dnslink
UDP: Code = Code(0x111)  # udp
P2P_WEBRTC_STAR: Code = Code(0x113)  # p2p-webrtc-star
P2P_WEBRTC_DIRECT: Code = Code(0x114)  # p2p-webrtc-direct
P2P_STARDUST: Code = Code(0x115)  # p2p-stardust
WEBRTC_DIRECT: Code = Code(0x118)  # webrtc-direct
WEBRTC: Code = Code(0x119)  # webrtc
P2P_CIRCUIT: Code = Code(0x122)  # p2p-circuit
UDT: Code = Code(0x12D)  # udt
UTP: Code = Code(0x12E)  # utp
UNIX: Code = Code(0x190)  # unix
THREAD: Code = Code(0x196)  # thread
P2P: Code = Code(0x1A5)  # p2p
HTTPS: Code = Code(0x1BB)  # https
ONION: Code = Code(0x1BC)  # onion
ONION3: Code = Code(0x1BD)  # onion3
GARLIC64: Code = Code(0x1BE)  # garlic64
GARLIC32: Code = Code(0x1BF)  # garlic32
TLS: Code = Code(0x1C0)  # tls
SNI: Code = Code(0x1C1)  # sni
NOISE: Code = Code(0x1C6)  # noise
SHS: Code = Code(0x1C8)  # shs
QUIC: Code = Code(0x1CC)  # quic
QUIC_V1: Code = Code(0x1CD)  # quic-v1
CERTHASH: Code = Code(0x1D2)  # certhash
WS: Code = Code(0x1DD)  # ws
WSS: Code = Code(0x1DE)  # wss
P2P_WEBSOCKET_STAR: Code = Code(0x1DF)  # p2p-websocket-star
HTTP: Code = Code(0x1E0)  # http
HTTP_PATH: Code = Code(0x1E1)  # http-path
LIBP2P_PEER_RECORD: Code = Code(0x301)  # libp2p-peer-record
LIBP2P_RELAY_RSVP: Code = Code(0x302)  # libp2p-relay-rsvp
MEMORYTRANSPORT: Code = Code(0x309)  # memorytransport
TRANSPORT_IPFS_GATEWAY_HTTP: Code = Code(0x920)  # transport-ipfs-gateway-http
TRANSPORT_FILECOIN_PIECE_HTTP: Code = Code(0x930)  # transport-filecoin-piece-http
PLAINTEXTV2: Code = Code(0x706C61)  # plaintextv2
SCION: Code = Code(0xD02000)  # scion

# Ipld
CIDV1: Code = Code(0x01)  # cidv1
CIDV2: Code = Code(0x02)  # cidv2
CIDV3: Code = Code(0x03)  # cidv3
IPCIDR: Code = Code(0x2B)  # ipcidr
RAW: Code = Code(0x55)  # raw
DAG_PB: Code = Code(0x70)  # dag-pb
DAG_CBOR: Code = Code(0x71)  # dag-cbor
GIT_RAW: Code = Code(0x78)  # git-raw
TORRENT_INFO: Code = Code(0x7B)  # torrent-info
TORRENT_FILE: Code = Code(0x7C)  # torrent-file
LEOFCOIN_BLOCK: Code = Code(0x81)  # leofcoin-block
LEOFCOIN_TX: Code = Code(0x82)  # leofcoin-tx
LEOFCOIN_PR: Code = Code(0x83)  # leofcoin-pr
DAG_JOSE: Code = Code(0x85)  # dag-jose
DAG_COSE: Code = Code(0x86)  # dag-cose
ETH_BLOCK: Code = Code(0x90)  # eth-block
ETH_BLOCK_LIST: Code = Code(0x91)  # eth-block-list
ETH_TX_TRIE: Code = Code(0x92)  # eth-tx-trie
ETH_TX: Code = Code(0x93)  # eth-tx
ETH_TX_RECEIPT_TRIE: Code = Code(0x94)  # eth-tx-receipt-trie
ETH_TX_RECEIPT: Code = Code(0x95)  # eth-tx-receipt
ETH_STATE_TRIE: Code = Code(0x96)  # eth-state-trie
ETH_ACCOUNT_SNAPSHOT: Code = Code(0x97)  # eth-account-snapshot
ETH_STORAGE_TRIE: Code = Code(0x98)  # eth-storage-trie
ETH_RECEIPT_LOG_TRIE: Code = Code(0x99)  # eth-receipt-log-trie
ETH_RECEIPT_LOG: Code = Code(0x9A)  # eth-receipt-log
BITCOIN_BLOCK: Code = Code(0xB0)  # bitcoin-block
BITCOIN_TX: Code = Code(0xB1)  # bitcoin-tx
BITCOIN_WITNESS_COMMITMENT: Code = Code(0xB2)  # bitcoin-witness-commitment
ZCASH_BLOCK: Code = Code(0xC0)  # zcash-block
ZCASH_TX: Code = Code(0xC1)  # zcash-tx
STELLAR_BLOCK: Code = Code(0xD0)  # stellar-block
STELLAR_TX: Code = Code(0xD1)  # stellar-tx
DECRED_BLOCK: Code = Code(0xE0)  # decred-block
DECRED_TX: Code = Code(0xE1)  # decred-tx
DASH_BLOCK: Code = Code(0xF0)  # dash-block
DASH_TX: Code = Code(0xF1)  # dash-tx
SWARM_MANIFEST: Code = Code(0xFA)  # swarm-manifest
SWARM_FEED: Code = Code(0xFB)  # swarm-feed
BEESON: Code = Code(0xFC)  # beeson
DAG_JSON: Code = Code(0x129)  # dag-json
SWHID_1_SNP: Code = Code(0x1F0)  # swhid-1-snp
BITTORRENT_PIECES_ROOT: Code = Code(0xB702)  # bittorrent-pieces-root

# Serialization
PROTOBUF: Code = Code(0x50)  # protobuf
CBOR: Code = Code(0x51)  # cbor
RLP: Code = Code(0x60)  # rlp
BENCODE: Code = Code(0x63)  # bencode
JSON: Code = Code(0x200)  # json
MESSAGEPACK: Code = Code(0x201)  # messagepack
CAR: Code = Code(0x202)  # car
X509_CERTIFICATE: Code = Code(0x210)  # x509-certificate
IPNS_RECORD: Code = Code(0x300)  # ipns-record
CAR_INDEX_SORTED: Code = Code(0x400)  # car-index-sorted
CAR_MULTIHASH_INDEX_SORTED: Code = Code(0x401)  # car-multihash-index-sorted
SSZ: Code = Code(0xB501)  # ssz
JSON_JCS: Code = Code(0xB601)  # json-jcs

# Multiformat
MULTICODEC: Code = Code(0x30)  # multicodec
MULTIHASH: Code = Code(0x31)  # multihash
MULTIADDR: Code = Code(0x32)  # multiaddr
MULTIBASE: Code = Code(0x33)  # multibase
VARSIG: Code = Code(0x34)  # varsig

# Key
SECP256K1_PUB: Code = Code(0xE7)  # secp256k1-pub
BLS12_381_G1_PUB: Code = Code(0xEA)  # bls12_381-g1-pub
BLS12_381_G2_PUB: Code = Code(0xEB)  # bls12_381-g2-pub
X25519_PUB: Code = Code(0xEC)  # x25519-pub
ED25519_PUB: Code = Code(0xED)  # ed25519-pub
BLS12_381_G1G2_PUB: Code = Code(0xEE)  # bls12_381-g1g2-pub
SR25519_PUB: Code = Code(0xEF)  # sr25519-pub
P256_PUB: Code = Code(0x1200)  # p256-pub
P384_PUB: Code = Code(0x1201)  # p384-pub
P521_PUB: Code = Code(0x1202)  # p521-pub
ED448_PUB: Code = Code(0x1203)  # ed448-pub
X448_PUB: Code = Code(0x1204)  # x448-pub
RSA_PUB: Code = Code(0x1205)  # rsa-pub
SM2_PUB: Code = Code(0x1206)  # sm2-pub
MLKEM_512_PUB: Code = Code(0x120B)  # mlkem-512-pub
MLKEM_768_PUB: Code = Code(0x120C)  # mlkem-768-pub
MLKEM_1024_PUB: Code = Code(0x120D)  # mlkem-1024-pub
ED25519_PRIV: Code = Code(0x1300)  # ed25519-priv
SECP256K1_PRIV: Code = Code(0x1301)  # secp256k1-priv
X25519_PRIV: Code = Code(0x1302)  # x25519-priv
SR25519_PRIV: Code = Code(0x1303)  # sr25519-priv
RSA_PRIV: Code = Code(0x1305)  # rsa-priv
P256_PRIV: Code = Code(0x1306)  # p256-priv
P384_PRIV: Code = Code(0x1307)  # p384-priv
P521_PRIV: Code = Code(0x1308)  # p521-priv
BLS12_381_G1_PRIV: Code = Code(0x1309)  # bls12_381-g1-priv
BLS12_381_G2_PRIV: Code = Code(0x130A)  # bls12_381-g2-priv
BLS12_381_G1G2_PRIV: Code = Code(0x130B)  # bls12_381-g1g2-priv
SM2_PRIV: Code = Code(0x1310)  # sm2-priv
ED448_PRIV: Code = Code(0x1311)  # ed448-priv
X448_PRIV: Code = Code(0x1312)  # x448-priv
MLKEM_512_PRIV: Code = Code(0x1313)  # mlkem-512-priv
MLKEM_768_PRIV: Code = Code(0x1314)  # mlkem-768-priv
MLKEM_1024_PRIV: Code = Code(0x1315)  # mlkem-1024-priv
JWK_JCS_PRIV: Code = Code(0x1316)  # jwk_jcs-priv
BLS12_381_G1_SIG: Code = Code(0xD0EA)  # bls12_381-g1-sig
BLS12_381_G2_SIG: Code = Code(0xD0EB)  # bls12_381-g2-sig
JWK_JCS_PUB: Code = Code(0xEB51)  # jwk_jcs-pub
BLS12_381_G1_MSIG: Code = Code(0xD01301)  # bls12_381-g1-msig
BLS12_381_G2_MSIG: Code = Code(0xD01302)  # bls12_381-g2-msig

# Namespace
PATH: Code = Code(0x2F)  # path
LBRY: Code = Code(0x8C)  # lbry
STREAMID: Code = Code(0xCE)  # streamid
IPNS: Code = Code(0xE5)  # ipns
ZERONET: Code = Code(0xE6)  # zeronet
WEBTRANSPORT: Code = Code(0x1D1)  # webtransport
TRANSPORT_BITSWAP: Code = Code(0x900)  # transport-bitswap
TRANSPORT_GRAPHSYNC_FILECOINV1: Code = Code(0x910)  # transport-graphsync-filecoinv1
NONSTANDARD_SIG: Code = Code(0xD000)  # nonstandard-sig
FIL_COMMITMENT_UNSEALED: Code = Code(0xF101)  # fil-commitment-unsealed
SKYNET_NS: Code = Code(0xB19910)  # skynet-ns
ARWEAVE_NS: Code = Code(0xB29910)  # arweave-ns
SUBSPACE_NS: Code = Code(0xB39910)  # subspace-ns
KUMANDRA_NS: Code = Code(0xB49910)  # kumandra-ns

# Other
AES_128: Code = Code(0xA0)  # aes-128
AES_192: Code = Code(0xA1)  # aes-192
AES_256: Code = Code(0xA2)  # aes-256
CHACHA_128: Code = Code(0xA3)  # chacha-128
CHACHA_256: Code = Code(0xA4)  # chacha-256
CAIP_50: Code = Code(0xCA)  # caip-50
IPLD: Code = Code(0xE2)  # ipld
IPFS: Code = Code(0xE3)  # ipfs
SWARM: Code = Code(0xE4)  # swarm
CRC32: Code = Code(0x132)  # crc32
CRC64_ECMA: Code = Code(0x164)  # crc64-ecma
CRC64_NVME: Code = Code(0x165)  # crc64-nvme
MULTIDID: Code = Code(0xD1D)  # multidid
VLAD: Code = Code(0x1207)  # vlad
PROVENANCE_LOG: Code = Code(0x1208)  # provenance-log
PROVENANCE_LOG_ENTRY: Code = Code(0x1209)  # provenance-log-entry
PROVENANCE_LOG_SCRIPT: Code = Code(0x120A)  # provenance-log-script
MULTISIG: Code = Code(0x1239)  # multisig
MULTIKEY: Code = Code(0x123A)  # multikey
NONCE: Code = Code(0x123B)  # nonce
AES_GCM_256: Code = Code(0x2000)  # aes-gcm-256
SILVERPINE: Code = Code(0x3F42)  # silverpine
CHACHA20_POLY1305: Code = Code(0xA000)  # chacha20-poly1305
XXH_32: Code = Code(0xB3E1)  # xxh-32
XXH_64: Code = Code(0xB3E2)  # xxh-64
XXH3_64: Code = Code(0xB3E3)  # xxh3-64
XXH3_128: Code = Code(0xB3E4)  # xxh3-128
RDFC_1: Code = Code(0xB403)  # rdfc-1
ISCC: Code = Code(0xCC01)  # iscc
ZEROXCERT_IMPRINT_256: Code = Code(0xCE11)  # zeroxcert-imprint-256
BCRYPT_PBKDF: Code = Code(0xD00D)  # bcrypt-pbkdf
ES256K: Code = Code(0xD0E7)  # es256k
EDDSA: Code = Code(0xD0ED)  # eddsa
EIP_191: Code = Code(0xD191)  # eip-191
ED2K: Code = Code(0xED20)  # ed2k
FIL_COMMITMENT_SEALED: Code = Code(0xF102)  # fil-commitment-sealed
SHELTER_CONTRACT_MANIFEST: Code = Code(0x511E00)  # shelter-contract-manifest
SHELTER_CONTRACT_TEXT: Code = Code(0x511E01)  # shelter-contract-text
SHELTER_CONTRACT_DATA: Code = Code(0x511E02)  # shelter-contract-data
SHELTER_FILE_MANIFEST: Code = Code(0x511E03)  # shelter-file-manifest
SHELTER_FILE_CHUNK: Code = Code(0x511E04)  # shelter-file-chunk
HOLOCHAIN_ADR_V0: Code = Code(0x807124)  # holochain-adr-v0
HOLOCHAIN_ADR_V1: Code = Code(0x817124)  # holochain-adr-v1
HOLOCHAIN_KEY_V0: Code = Code(0x947124)  # holochain-key-v0
HOLOCHAIN_KEY_V1: Code = Code(0x957124)  # holochain-key-v1
HOLOCHAIN_SIG_V0: Code = Code(0xA27124)  # holochain-sig-v0
HOLOCHAIN_SIG_V1: Code = Code(0xA37124)  # holochain-sig-v1
ES256: Code = Code(0xD01200)  # es256
ES384: Code = Code(0xD01201)  # es384
ES512: Code = Code(0xD01202)  # es512
RS256: Code = Code(0xD01205)  # rs256
ES256K_MSIG: Code = Code(0xD01300)  # es256k-msig
EDDSA_MSIG: Code = Code(0xD01303)  # eddsa-msig
LAMPORT_MSIG: Code = Code(0xD01306)  # lamport-msig
ES256_MSIG: Code = Code(0xD01308)  # es256-msig
ES384_MSIG: Code = Code(0xD01309)  # es384-msig
ES521_MSIG: Code = Code(0xD0130A)  # es521-msig
RS256_MSIG: Code = Code(0xD0130B)  # rs256-msig

__all__ = [
    "AES_128",
    "AES_192",
    "AES_256",
    "AES_GCM_256",
    "ARWEAVE_NS",
    "BCRYPT_PBKDF",
    "BEESON",
    "BENCODE",
    "BITCOIN_BLOCK",
    "BITCOIN_TX",
    "BITCOIN_WITNESS_COMMITMENT",
    "BITTORRENT_PIECES_ROOT",
    "BLAKE2B_8",
    "BLAKE2B_16",
    "BLAKE2B_24",
    "BLAKE2B_32",
    "BLAKE2B_40",
    "BLAKE2B_48",
    "BLAKE2B_56",
    "BLAKE2B_64",
    "BLAKE2B_72",
    "BLAKE2B_80",
    "BLAKE2B_88",
    "BLAKE2B_96",
    "BLAKE2B_104",
    "BLAKE2B_112",
    "BLAKE2B_120",
    "BLAKE2B_128",
    "BLAKE2B_136",
    "BLAKE2B_144",
    "BLAKE2B_152",
    "BLAKE2B_160",
    "BLAKE2B_168",
    "BLAKE2B_176",
    "BLAKE2B_184",
    "BLAKE2B_192",
    "BLAKE2B_200",
    "BLAKE2B_208",
    "BLAKE2B_216",
    "BLAKE2B_224",
    "BLAKE2B_232",
    "BLAKE2B_240",
    "BLAKE2B_248",
    "BLAKE2B_256",
    "BLAKE2B_264",
    "BLAKE2B_272",
    "BLAKE2B_280",
    "BLAKE2B_288",
    "BLAKE2B_296",
    "BLAKE2B_304",
    "BLAKE2B_312",
    "BLAKE2B_320",
    "BLAKE2B_328",
    "BLAKE2B_336",
    "BLAKE2B_344",
    "BLAKE2B_352",
    "BLAKE2B_360",
    "BLAKE2B_368",
    "BLAKE2B_376",
    "BLAKE2B_384",
    "BLAKE2B_392",
    "BLAKE2B_400",
    "BLAKE2B_408",
    "BLAKE2B_416",
    "BLAKE2B_424",
    "BLAKE2B_432",
    "BLAKE2B_440",
    "BLAKE2B_448",
    "BLAKE2B_456",
    "BLAKE2B_464",
    "BLAKE2B_472",
    "BLAKE2B_480",
    "BLAKE2B_488",
    "BLAKE2B_496",
    "BLAKE2B_504",
    "BLAKE2B_512",
    "BLAKE2S_8",
    "BLAKE2S_16",
    "BLAKE2S_24",
    "BLAKE2S_32",
    "BLAKE2S_40",
    "BLAKE2S_48",
    "BLAKE2S_56",
    "BLAKE2S_64",
    "BLAKE2S_72",
    "BLAKE2S_80",
    "BLAKE2S_88",
    "BLAKE2S_96",
    "BLAKE2S_104",
    "BLAKE2S_112",
    "BLAKE2S_120",
    "BLAKE2S_128",
    "BLAKE2S_136",
    "BLAKE2S_144",
    "BLAKE2S_152",
    "BLAKE2S_160",
    "BLAKE2S_168",
    "BLAKE2S_176",
    "BLAKE2S_184",
    "BLAKE2S_192",
    "BLAKE2S_200",
    "BLAKE2S_208",
    "BLAKE2S_216",
    "BLAKE2S_224",
    "BLAKE2S_232",
    "BLAKE2S_240",
    "BLAKE2S_248",
    "BLAKE2S_256",
    "BLAKE3",
    "BLAKE3_HASHSEQ",
    "BLS12_381_G1G2_PRIV",
    "BLS12_381_G1G2_PUB",
    "BLS12_381_G1_MSIG",
    "BLS12_381_G1_PRIV",
    "BLS12_381_G1_PRIV_SHARE",
    "BLS12_381_G1_PUB",
    "BLS12_381_G1_PUB_SHARE",
    "BLS12_381_G1_SHARE_MSIG",
    "BLS12_381_G1_SIG",
    "BLS12_381_G2_MSIG",
    "BLS12_381_G2_PRIV",
    "BLS12_381_G2_PRIV_SHARE",
    "BLS12_381_G2_PUB",
    "BLS12_381_G2_PUB_SHARE",
    "BLS12_381_G2_SHARE_MSIG",
    "BLS12_381_G2_SIG",
    "CAIP_50",
    "CAR",
    "CAR_INDEX_SORTED",
    "CAR_MULTIHASH_INDEX_SORTED",
    "CBOR",
    "CERTHASH",
    "CHACHA20_POLY1305",
    "CHACHA_128",
    "CHACHA_256",
    "CIDV1",
    "CIDV2",
    "CIDV3",
    "CRC32",
    "CRC64_ECMA",
    "CRC64_NVME",
    "DAG_CBOR",
    "DAG_COSE",
    "DAG_JOSE",
    "DAG_JSON",
    "DAG_PB",
    "DASH_BLOCK",
    "DASH_TX",
    "DBL_SHA2_256",
    "DCCP",
    "DECRED_BLOCK",
    "DECRED_TX",
    "DNS",
    "DNS4",
    "DNS6",
    "DNSADDR",
    "DNSLINK",
    "ED2K",
    "ED448_PRIV",
    "ED448_PUB",
    "ED25519_PRIV",
    "ED25519_PUB",
    "EDDSA",
    "EDDSA_MSIG",
    "EIP_191",
    "ES256",
    "ES256K",
    "ES256K_MSIG",
    "ES256_MSIG",
    "ES384",
    "ES384_MSIG",
    "ES512",
    "ES521_MSIG",
    "ETH_ACCOUNT_SNAPSHOT",
    "ETH_BLOCK",
    "ETH_BLOCK_LIST",
    "ETH_RECEIPT_LOG",
    "ETH_RECEIPT_LOG_TRIE",
    "ETH_STATE_TRIE",
    "ETH_STORAGE_TRIE",
    "ETH_TX",
    "ETH_TX_RECEIPT",
    "ETH_TX_RECEIPT_TRIE",
    "ETH_TX_TRIE",
    "FIL_COMMITMENT_SEALED",
    "FIL_COMMITMENT_UNSEALED",
    "FR32_SHA256_TRUNC254_PADBINTREE",
    "GARLIC32",
    "GARLIC64",
    "GIT_RAW",
    "HOLOCHAIN_ADR_V0",
    "HOLOCHAIN_ADR_V1",
    "HOLOCHAIN_KEY_V0",
    "HOLOCHAIN_KEY_V1",
    "HOLOCHAIN_SIG_V0",
    "HOLOCHAIN_SIG_V1",
    "HTTP",
    "HTTPS",
    "HTTP_PATH",
    "IDENTITY",
    "IP4",
    "IP6",
    "IP6ZONE",
    "IPCIDR",
    "IPFS",
    "IPLD",
    "IPNS",
    "IPNS_RECORD",
    "ISCC",
    "JSON",
    "JSON_JCS",
    "JWK_JCS_PRIV",
    "JWK_JCS_PUB",
    "KANGAROOTWELVE",
    "KECCAK_224",
    "KECCAK_256",
    "KECCAK_384",
    "KECCAK_512",
    "KUMANDRA_NS",
    "LAMPORT_MSIG",
    "LAMPORT_SHA3_256_PRIV",
    "LAMPORT_SHA3_256_PRIV_SHARE",
    "LAMPORT_SHA3_256_PUB",
    "LAMPORT_SHA3_256_SIG",
    "LAMPORT_SHA3_256_SIG_SHARE",
    "LAMPORT_SHA3_384_PRIV",
    "LAMPORT_SHA3_384_PRIV_SHARE",
    "LAMPORT_SHA3_384_PUB",
    "LAMPORT_SHA3_384_SIG",
    "LAMPORT_SHA3_384_SIG_SHARE",
    "LAMPORT_SHA3_512_PRIV",
    "LAMPORT_SHA3_512_PRIV_SHARE",
    "LAMPORT_SHA3_512_PUB",
    "LAMPORT_SHA3_512_SIG",
    "LAMPORT_SHA3_512_SIG_SHARE",
    "LAMPORT_SHARE_MSIG",
    "LBRY",
    "LEOFCOIN_BLOCK",
    "LEOFCOIN_PR",
    "LEOFCOIN_TX",
    "LIBP2P_KEY",
    "LIBP2P_PEER_RECORD",
    "LIBP2P_RELAY_RSVP",
    "MD4",
    "MD5",
    "MEMORYTRANSPORT",
    "MESSAGEPACK",
    "MLKEM_512_PRIV",
    "MLKEM_512_PUB",
    "MLKEM_768_PRIV",
    "MLKEM_768_PUB",
    "MLKEM_1024_PRIV",
    "MLKEM_1024_PUB",
    "MULTIADDR",
    "MULTIBASE",
    "MULTICODEC",
    "MULTIDID",
    "MULTIHASH",
    "MULTIKEY",
    "MULTISIG",
    "MURMUR3_32",
    "MURMUR3_X64_64",
    "MURMUR3_X64_128",
    "NOISE",
    "NONCE",
    "NONSTANDARD_SIG",
    "ONION",
    "ONION3",
    "P2P",
    "P2P_CIRCUIT",
    "P2P_STARDUST",
    "P2P_WEBRTC_DIRECT",
    "P2P_WEBRTC_STAR",
    "P2P_WEBSOCKET_STAR",
    "P256_PRIV",
    "P256_PUB",
    "P384_PRIV",
    "P384_PUB",
    "P521_PRIV",
    "P521_PUB",
    "PATH",
    "PLAINTEXTV2",
    "POSEIDON_BLS12_381_A2_FC1",
    "POSEIDON_BLS12_381_A2_FC1_SC",
    "PROTOBUF",
    "PROVENANCE_LOG",
    "PROVENANCE_LOG_ENTRY",
    "PROVENANCE_LOG_SCRIPT",
    "QUIC",
    "QUIC_V1",
    "RAW",
    "RDFC_1",
    "RIPEMD_128",
    "RIPEMD_160",
    "RIPEMD_256",
    "RIPEMD_320",
    "RLP",
    "RS256",
    "RS256_MSIG",
    "RSA_PRIV",
    "RSA_PUB",
    "SCION",
    "SCTP",
    "SECP256K1_PRIV",
    "SECP256K1_PUB",
    "SHA1",
    "SHA2_224",
    "SHA2_256",
    "SHA2_256_CHUNKED",
    "SHA2_256_TRUNC254_PADDED",
    "SHA2_384",
    "SHA2_512",
    "SHA2_512_224",
    "SHA2_512_256",
    "SHA3_224",
    "SHA3_256",
    "SHA3_384",
    "SHA3_512",
    "SHA256A",
    "SHAKE_128",
    "SHAKE_256",
    "SHELTER_CONTRACT_DATA",
    "SHELTER_CONTRACT_MANIFEST",
    "SHELTER_CONTRACT_TEXT",
    "SHELTER_FILE_CHUNK",
    "SHELTER_FILE_MANIFEST",
    "SHS",
    "SILVERPINE",
    "SKEIN256_8",
    "SKEIN256_16",
    "SKEIN256_24",
    "SKEIN256_32",
    "SKEIN256_40",
    "SKEIN256_48",
    "SKEIN256_56",
    "SKEIN256_64",
    "SKEIN256_72",
    "SKEIN256_80",
    "SKEIN256_88",
    "SKEIN256_96",
    "SKEIN256_104",
    "SKEIN256_112",
    "SKEIN256_120",
    "SKEIN256_128",
    "SKEIN256_136",
    "SKEIN256_144",
    "SKEIN256_152",
    "SKEIN256_160",
    "SKEIN256_168",
    "SKEIN256_176",
    "SKEIN256_184",
    "SKEIN256_192",
    "SKEIN256_200",
    "SKEIN256_208",
    "SKEIN256_216",
    "SKEIN256_224",
    "SKEIN256_232",
    "SKEIN256_240",
    "SKEIN256_248",
    "SKEIN256_256",
    "SKEIN512_8",
    "SKEIN512_16",
    "SKEIN512_24",
    "SKEIN512_32",
    "SKEIN512_40",
    "SKEIN512_48",
    "SKEIN512_56",
    "SKEIN512_64",
    "SKEIN512_72",
    "SKEIN512_80",
    "SKEIN512_88",
    "SKEIN512_96",
    "SKEIN512_104",
    "SKEIN512_112",
    "SKEIN512_120",
    "SKEIN512_128",
    "SKEIN512_136",
    "SKEIN512_144",
    "SKEIN512_152",
    "SKEIN512_160",
    "SKEIN512_168",
    "SKEIN512_176",
    "SKEIN512_184",
    "SKEIN512_192",
    "SKEIN512_200",
    "SKEIN512_208",
    "SKEIN512_216",
    "SKEIN512_224",
    "SKEIN512_232",
    "SKEIN512_240",
    "SKEIN512_248",
    "SKEIN512_256",
    "SKEIN512_264",
    "SKEIN512_272",
    "SKEIN512_280",
    "SKEIN512_288",
    "SKEIN512_296",
    "SKEIN512_304",
    "SKEIN512_312",
    "SKEIN512_320",
    "SKEIN512_328",
    "SKEIN512_336",
    "SKEIN512_344",
    "SKEIN512_352",
    "SKEIN512_360",
    "SKEIN512_368",
    "SKEIN512_376",
    "SKEIN512_384",
    "SKEIN512_392",
    "SKEIN512_400",
    "SKEIN512_408",
    "SKEIN512_416",
    "SKEIN512_424",
    "SKEIN512_432",
    "SKEIN512_440",
    "SKEIN512_448",
    "SKEIN512_456",
    "SKEIN512_464",
    "SKEIN512_472",
    "SKEIN512_480",
    "SKEIN512_488",
    "SKEIN512_496",
    "SKEIN512_504",
    "SKEIN512_512",
    "SKEIN1024_8",
    "SKEIN1024_16",
    "SKEIN1024_24",
    "SKEIN1024_32",
    "SKEIN1024_40",
    "SKEIN1024_48",
    "SKEIN1024_56",
    "SKEIN1024_64",
    "SKEIN1024_72",
    "SKEIN1024_80",
    "SKEIN1024_88",
    "SKEIN1024_96",
    "SKEIN1024_104",
    "SKEIN1024_112",
    "SKEIN1024_120",
    "SKEIN1024_128",
    "SKEIN1024_136",
    "SKEIN1024_144",
    "SKEIN1024_152",
    "SKEIN1024_160",
    "SKEIN1024_168",
    "SKEIN1024_176",
    "SKEIN1024_184",
    "SKEIN1024_192",
    "SKEIN1024_200",
    "SKEIN1024_208",
    "SKEIN1024_216",
    "SKEIN1024_224",
    "SKEIN1024_232",
    "SKEIN1024_240",
    "SKEIN1024_248",
    "SKEIN1024_256",
    "SKEIN1024_264",
    "SKEIN1024_272",
    "SKEIN1024_280",
    "SKEIN1024_288",
    "SKEIN1024_296",
    "SKEIN1024_304",
    "SKEIN1024_312",
    "SKEIN1024_320",
    "SKEIN1024_328",
    "SKEIN1024_336",
    "SKEIN1024_344",
    "SKEIN1024_352",
    "SKEIN1024_360",
    "SKEIN1024_368",
    "SKEIN1024_376",
    "SKEIN1024_384",
    "SKEIN1024_392",
    "SKEIN1024_400",
    "SKEIN1024_408",
    "SKEIN1024_416",
    "SKEIN1024_424",
    "SKEIN1024_432",
    "SKEIN1024_440",
    "SKEIN1024_448",
    "SKEIN1024_456",
    "SKEIN1024_464",
    "SKEIN1024_472",
    "SKEIN1024_480",
    "SKEIN1024_488",
    "SKEIN1024_496",
    "SKEIN1024_504",
    "SKEIN1024_512",
    "SKEIN1024_520",
    "SKEIN1024_528",
    "SKEIN1024_536",
    "SKEIN1024_544",
    "SKEIN1024_552",
    "SKEIN1024_560",
    "SKEIN1024_568",
    "SKEIN1024_576",
    "SKEIN1024_584",
    "SKEIN1024_592",
    "SKEIN1024_600",
    "SKEIN1024_608",
    "SKEIN1024_616",
    "SKEIN1024_624",
    "SKEIN1024_632",
    "SKEIN1024_640",
    "SKEIN1024_648",
    "SKEIN1024_656",
    "SKEIN1024_664",
    "SKEIN1024_672",
    "SKEIN1024_680",
    "SKEIN1024_688",
    "SKEIN1024_696",
    "SKEIN1024_704",
    "SKEIN1024_712",
    "SKEIN1024_720",
    "SKEIN1024_728",
    "SKEIN1024_736",
    "SKEIN1024_744",
    "SKEIN1024_752",
    "SKEIN1024_760",
    "SKEIN1024_768",
    "SKEIN1024_776",
    "SKEIN1024_784",
    "SKEIN1024_792",
    "SKEIN1024_800",
    "SKEIN1024_808",
    "SKEIN1024_816",
    "SKEIN1024_824",
    "SKEIN1024_832",
    "SKEIN1024_840",
    "SKEIN1024_848",
    "SKEIN1024_856",
    "SKEIN1024_864",
    "SKEIN1024_872",
    "SKEIN1024_880",
    "SKEIN1024_888",
    "SKEIN1024_896",
    "SKEIN1024_904",
    "SKEIN1024_912",
    "SKEIN1024_920",
    "SKEIN1024_928",
    "SKEIN1024_936",
    "SKEIN1024_944",
    "SKEIN1024_952",
    "SKEIN1024_960",
    "SKEIN1024_968",
    "SKEIN1024_976",
    "SKEIN1024_984",
    "SKEIN1024_992",
    "SKEIN1024_1000",
    "SKEIN1024_1008",
    "SKEIN1024_1016",
    "SKEIN1024_1024",
    "SKYNET_NS",
    "SM2_PRIV",
    "SM2_PUB",
    "SM3_256",
    "SNI",
    "SR25519_PRIV",
    "SR25519_PUB",
    "SSZ",
    "SSZ_SHA2_256_BMT",
    "STELLAR_BLOCK",
    "STELLAR_TX",
    "STREAMID",
    "SUBSPACE_NS",
    "SWARM",
    "SWARM_FEED",
    "SWARM_MANIFEST",
    "SWHID_1_SNP",
    "TCP",
    "THREAD",
    "TLS",
    "TORRENT_FILE",
    "TORRENT_INFO",
    "TRANSPORT_BITSWAP",
    "TRANSPORT_FILECOIN_PIECE_HTTP",
    "TRANSPORT_GRAPHSYNC_FILECOINV1",
    "TRANSPORT_IPFS_GATEWAY_HTTP",
    "UDP",
    "UDT",
    "UNIX",
    "UTP",
    "VARSIG",
    "VLAD",
    "WEBRTC",
    "WEBRTC_DIRECT",
    "WEBTRANSPORT",
    "WS",
    "WSS",
    "X11",
    "X448_PRIV",
    "X448_PUB",
    "X509_CERTIFICATE",
    "X25519_PRIV",
    "X25519_PUB",
    "XXH3_64",
    "XXH3_128",
    "XXH_32",
    "XXH_64",
    "ZCASH_BLOCK",
    "ZCASH_TX",
    "ZERONET",
    "ZEROXCERT_IMPRINT_256",
]
