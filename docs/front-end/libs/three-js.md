# Three.js Interview Questions and Answers

_Last updated: October 28, 2026_

90 Three.js interview questions with answers, split into three levels: 30 easy, 30 moderate and 30 advanced.

The answers target recent Three.js releases (r186 at the time of writing). They cover the classic `WebGLRenderer` that most projects still use, plus the newer `WebGPURenderer` and TSL. Older APIs that you will still see in tutorials and existing code (like `Clock`, `RGBELoader` or legacy lighting) are mentioned where it makes sense.

## Table of Contents

- [Easy Questions (1-30)](#easy-questions-1-30)
- [Moderate Questions (31-60)](#moderate-questions-31-60)
- [Advanced Questions (61-90)](#advanced-questions-61-90)

### Easy Questions (1-30)

- [1: What is Three.js?](#1-what-is-threejs)
- [2: What is the difference between Three.js and WebGL?](#2-what-is-the-difference-between-threejs-and-webgl)
- [3: How do you install Three.js and import it?](#3-how-do-you-install-threejs-and-import-it)
- [4: What are the three things you always need to render something?](#4-what-are-the-three-things-you-always-need-to-render-something)
- [5: What is a Scene?](#5-what-is-a-scene)
- [6: What are the parameters of a PerspectiveCamera?](#6-what-are-the-parameters-of-a-perspectivecamera)
- [7: What is an OrthographicCamera and when would you use it?](#7-what-is-an-orthographiccamera-and-when-would-you-use-it)
- [8: What is a Mesh?](#8-what-is-a-mesh)
- [9: What built-in geometries does Three.js have?](#9-what-built-in-geometries-does-threejs-have)
- [10: What is BufferGeometry?](#10-what-is-buffergeometry)
- [11: What are the most common materials and how are they different?](#11-what-are-the-most-common-materials-and-how-are-they-different)
- [12: Why does my object render completely black?](#12-why-does-my-object-render-completely-black)
- [13: What types of lights are there?](#13-what-types-of-lights-are-there)
- [14: How do you create an animation loop?](#14-how-do-you-create-an-animation-loop)
- [15: How do you move, rotate and scale an object?](#15-how-do-you-move-rotate-and-scale-an-object)
- [16: What is Object3D and what is the scene graph?](#16-what-is-object3d-and-what-is-the-scene-graph)
- [17: How do you handle window resizing?](#17-how-do-you-handle-window-resizing)
- [18: What does renderer.setPixelRatio do?](#18-what-does-renderersetpixelratio-do)
- [19: How do you load and apply a texture?](#19-how-do-you-load-and-apply-a-texture)
- [20: What are OrbitControls?](#20-what-are-orbitcontrols)
- [21: How do you load a 3D model?](#21-how-do-you-load-a-3d-model)
- [22: Why is glTF the recommended model format?](#22-why-is-gltf-the-recommended-model-format)
- [23: What coordinate system does Three.js use?](#23-what-coordinate-system-does-threejs-use)
- [24: How do you convert degrees to radians?](#24-how-do-you-convert-degrees-to-radians)
- [25: What helpers does Three.js provide for debugging?](#25-what-helpers-does-threejs-provide-for-debugging)
- [26: How do you add fog?](#26-how-do-you-add-fog)
- [27: How do you set the background of a scene?](#27-how-do-you-set-the-background-of-a-scene)
- [28: What is Vector3 and what can you do with it?](#28-what-is-vector3-and-what-can-you-do-with-it)
- [29: How do you get rid of jagged edges?](#29-how-do-you-get-rid-of-jagged-edges)
- [30: How are Three.js versions numbered?](#30-how-are-threejs-versions-numbered)

### Moderate Questions (31-60)

- [31: How do you detect which object the user clicked on?](#31-how-do-you-detect-which-object-the-user-clicked-on)
- [32: Why should animations use delta time instead of a fixed step per frame?](#32-why-should-animations-use-delta-time-instead-of-a-fixed-step-per-frame)
- [33: How do you play animations from a glTF model?](#33-how-do-you-play-animations-from-a-gltf-model)
- [34: How do you enable shadows?](#34-how-do-you-enable-shadows)
- [35: What are the main properties of MeshStandardMaterial?](#35-what-are-the-main-properties-of-meshstandardmaterial)
- [36: How do you add realistic lighting with an HDR environment map?](#36-how-do-you-add-realistic-lighting-with-an-hdr-environment-map)
- [37: What is color management and tone mapping in Three.js?](#37-what-is-color-management-and-tone-mapping-in-threejs)
- [38: What are the common texture settings you need to know?](#38-what-are-the-common-texture-settings-you-need-to-know)
- [39: How do you free GPU memory in Three.js?](#39-how-do-you-free-gpu-memory-in-threejs)
- [40: What is InstancedMesh and when should you use it?](#40-what-is-instancedmesh-and-when-should-you-use-it)
- [41: What is a draw call and how do you reduce them?](#41-what-is-a-draw-call-and-how-do-you-reduce-them)
- [42: How do you monitor performance in a Three.js app?](#42-how-do-you-monitor-performance-in-a-threejs-app)
- [43: How do you create a custom geometry?](#43-how-do-you-create-a-custom-geometry)
- [44: What is the difference between ShaderMaterial and RawShaderMaterial?](#44-what-is-the-difference-between-shadermaterial-and-rawshadermaterial)
- [45: How do you change a built-in material's shader without rewriting it?](#45-how-do-you-change-a-built-in-materials-shader-without-rewriting-it)
- [46: How do you add post-processing effects like bloom?](#46-how-do-you-add-post-processing-effects-like-bloom)
- [47: What is a render target and what can you do with it?](#47-what-is-a-render-target-and-what-can-you-do-with-it)
- [48: Why do transparent objects look wrong, and how do you fix it?](#48-why-do-transparent-objects-look-wrong-and-how-do-you-fix-it)
- [49: What is the difference between local and world coordinates?](#49-what-is-the-difference-between-local-and-world-coordinates)
- [50: Why are quaternions used for rotation instead of Euler angles?](#50-why-are-quaternions-used-for-rotation-instead-of-euler-angles)
- [51: How do you make glTF models smaller and faster to load?](#51-how-do-you-make-gltf-models-smaller-and-faster-to-load)
- [52: How do you show a loading progress bar?](#52-how-do-you-show-a-loading-progress-bar)
- [53: What is React Three Fiber?](#53-what-is-react-three-fiber)
- [54: How do you show HTML labels attached to 3D objects?](#54-how-do-you-show-html-labels-attached-to-3d-objects)
- [55: What are layers and what can you use them for?](#55-what-are-layers-and-what-can-you-use-them-for)
- [56: Why does LineBasicMaterial ignore linewidth?](#56-why-does-linebasicmaterial-ignore-linewidth)
- [57: What is frustum culling and when can it cause problems?](#57-what-is-frustum-culling-and-when-can-it-cause-problems)
- [58: What is z-fighting and how do you fix it?](#58-what-is-z-fighting-and-how-do-you-fix-it)
- [59: What tools do you use to debug a Three.js scene?](#59-what-tools-do-you-use-to-debug-a-threejs-scene)
- [60: What are morph targets?](#60-what-are-morph-targets)

### Advanced Questions (61-90)

- [61: What is WebGPURenderer and how is it different from WebGLRenderer?](#61-what-is-webgpurenderer-and-how-is-it-different-from-webglrenderer)
- [62: What is TSL and why was it introduced?](#62-what-is-tsl-and-why-was-it-introduced)
- [63: How do you run a compute shader in Three.js?](#63-how-do-you-run-a-compute-shader-in-threejs)
- [64: What happens inside renderer.render(scene, camera)?](#64-what-happens-inside-rendererrenderscene-camera)
- [65: Why does the app freeze for a moment when a new object appears, and how do you fix it?](#65-why-does-the-app-freeze-for-a-moment-when-a-new-object-appears-and-how-do-you-fix-it)
- [66: A scene has 20,000 objects and runs at 15 FPS. How do you approach it?](#66-a-scene-has-20000-objects-and-runs-at-15-fps-how-do-you-approach-it)
- [67: When do you pick InstancedMesh, BatchedMesh or merged geometry?](#67-when-do-you-pick-instancedmesh-batchedmesh-or-merged-geometry)
- [68: How do you handle very large models and textures without running out of GPU memory?](#68-how-do-you-handle-very-large-models-and-textures-without-running-out-of-gpu-memory)
- [69: How do matrix updates work, and how can you reduce their cost?](#69-how-do-matrix-updates-work-and-how-can-you-reduce-their-cost)
- [70: Raycasting against a detailed model is slow. How do you make it faster?](#70-raycasting-against-a-detailed-model-is-slow-how-do-you-make-it-faster)
- [71: How do you get good-looking shadows without killing performance?](#71-how-do-you-get-good-looking-shadows-without-killing-performance)
- [72: How do you deal with depth precision problems in large scenes?](#72-how-do-you-deal-with-depth-precision-problems-in-large-scenes)
- [73: How do you apply bloom only to some objects?](#73-how-do-you-apply-bloom-only-to-some-objects)
- [74: What is a lost WebGL context and how do you handle it?](#74-what-is-a-lost-webgl-context-and-how-do-you-handle-it)
- [75: How do you run Three.js in a Web Worker?](#75-how-do-you-run-threejs-in-a-web-worker)
- [76: How do you avoid memory leaks when using Three.js in a single-page app?](#76-how-do-you-avoid-memory-leaks-when-using-threejs-in-a-single-page-app)
- [77: Why does cloning a glTF character break its animation, and how do you clone it correctly?](#77-why-does-cloning-a-gltf-character-break-its-animation-and-how-do-you-clone-it-correctly)
- [78: How would you render a million points efficiently?](#78-how-would-you-render-a-million-points-efficiently)
- [79: Objects far from the origin start shaking. Why, and how do you fix it?](#79-objects-far-from-the-origin-start-shaking-why-and-how-do-you-fix-it)
- [80: How do you make a Three.js scene run well on low-end mobile devices?](#80-how-do-you-make-a-threejs-scene-run-well-on-low-end-mobile-devices)
- [81: How do you render only when something changes?](#81-how-do-you-render-only-when-something-changes)
- [82: What do you check when upgrading an old project to a recent Three.js version?](#82-what-do-you-check-when-upgrading-an-old-project-to-a-recent-threejs-version)
- [83: How do light intensities work in physically based lighting?](#83-how-do-light-intensities-work-in-physically-based-lighting)
- [84: How do you build a WebXR (VR or AR) experience with Three.js?](#84-how-do-you-build-a-webxr-vr-or-ar-experience-with-threejs)
- [85: How do you write your own post-processing pass with EffectComposer?](#85-how-do-you-write-your-own-post-processing-pass-with-effectcomposer)
- [86: How do you add physics to a Three.js scene?](#86-how-do-you-add-physics-to-a-threejs-scene)
- [87: Why does a texture from another domain fail to load, and how do you fix it?](#87-why-does-a-texture-from-another-domain-fail-to-load-and-how-do-you-fix-it)
- [88: How do you structure a large Three.js application?](#88-how-do-you-structure-a-large-threejs-application)
- [89: A model looks different in Three.js than in Blender. What do you check?](#89-a-model-looks-different-in-threejs-than-in-blender-what-do-you-check)
- [90: How do you choose between plain Three.js, React Three Fiber and a full engine like Babylon.js or PlayCanvas?](#90-how-do-you-choose-between-plain-threejs-react-three-fiber-and-a-full-engine-like-babylonjs-or-playcanvas)

---

# Easy Questions (1-30)

## 1: What is Three.js?

Three.js is a JavaScript library for drawing 3D graphics in the browser. Under the hood it uses WebGL (and now also WebGPU), but it hides most of the low-level work. Instead of writing shaders and managing GPU buffers by hand, you create a scene, add objects, lights and a camera, and let the renderer draw it.

It is used for product configurators, data visualization, games, portfolio sites, maps, architecture previews and AR/VR experiences.

## 2: What is the difference between Three.js and WebGL?

WebGL is a low-level browser API. With raw WebGL you write vertex and fragment shaders, create buffers, upload data, set up matrices and issue draw calls yourself. Drawing a single lit cube takes a lot of code.

Three.js is built on top of WebGL. It gives you ready objects like cameras, lights, materials, geometries, loaders and controls. You still can drop down to custom shaders when you need to, but most of the time you work with higher-level objects. The trade-off is a bit of overhead and less control over every GPU call.

## 3: How do you install Three.js and import it?

With npm:

```bash
npm install three
```

```js
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
```

The core library is imported from `three`. Extra features like controls, loaders and post-processing live in the addons folder and are imported from `three/addons/...`.

Without a bundler you can use an import map:

```html
<script type="importmap">
  {
    "imports": {
      "three": "https://cdn.jsdelivr.net/npm/three@0.186.0/build/three.module.js",
      "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.186.0/examples/jsm/"
    }
  }
</script>
```

## 4: What are the three things you always need to render something?

A **scene**, a **camera** and a **renderer**. The scene holds your objects, the camera decides what part of the scene you see, and the renderer draws the scene from the camera's point of view onto a canvas.

```js
import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  innerWidth / innerHeight,
  0.1,
  100,
);
camera.position.z = 3;

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);

const cube = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshBasicMaterial({ color: 0x44aa88 }),
);
scene.add(cube);

renderer.setAnimationLoop(() => {
  cube.rotation.y += 0.01;
  renderer.render(scene, camera);
});
```

## 5: What is a Scene?

`THREE.Scene` is the root container for everything you want to draw: meshes, lights, cameras, groups and so on. It also has a few scene-wide settings like `background`, `environment` and `fog`.

Only objects added to the scene (directly or through a parent) are rendered. If you create a mesh and forget `scene.add(mesh)`, it won't show up.

## 6: What are the parameters of a PerspectiveCamera?

```js
new THREE.PerspectiveCamera(fov, aspect, near, far);
```

- **fov**: vertical field of view in degrees. 45-75 is common.
- **aspect**: width divided by height of the canvas. If it is wrong, the image looks stretched.
- **near**: the closest distance the camera can see.
- **far**: the farthest distance the camera can see.

Anything closer than `near` or farther than `far` is clipped. After changing any of these values you must call `camera.updateProjectionMatrix()`.

## 7: What is an OrthographicCamera and when would you use it?

An orthographic camera has no perspective. Objects keep the same size no matter how far they are from the camera, and parallel lines stay parallel.

```js
const frustumSize = 10;
const aspect = innerWidth / innerHeight;
const camera = new THREE.OrthographicCamera(
  (-frustumSize * aspect) / 2,
  (frustumSize * aspect) / 2,
  frustumSize / 2,
  -frustumSize / 2,
  0.1,
  100,
);
```

It is used for 2D games, isometric views, CAD and technical drawings, maps, UI overlays and for the shadow camera of directional lights.

## 8: What is a Mesh?

A `Mesh` is a visible 3D object. It combines a **geometry** (the shape, made of vertices and triangles) and a **material** (how the surface looks).

```js
const geometry = new THREE.SphereGeometry(1, 32, 16);
const material = new THREE.MeshStandardMaterial({ color: "orange" });
const sphere = new THREE.Mesh(geometry, material);
scene.add(sphere);
```

The same geometry and material can be shared by many meshes, which saves memory.

## 9: What built-in geometries does Three.js have?

The common ones are `BoxGeometry`, `SphereGeometry`, `PlaneGeometry`, `CylinderGeometry`, `ConeGeometry`, `CircleGeometry`, `TorusGeometry`, `TorusKnotGeometry`, `CapsuleGeometry`, `RingGeometry` and `IcosahedronGeometry`. There are also `LatheGeometry`, `ExtrudeGeometry`, `ShapeGeometry` and `TubeGeometry` for building shapes from 2D outlines or curves.

Most of them accept segment parameters. More segments make a smoother shape but cost more vertices.

## 10: What is BufferGeometry?

`BufferGeometry` is the class that stores the actual vertex data: positions, normals, UVs, colors and optionally an index. Each of these is stored as a `BufferAttribute` backed by a typed array, which can be sent straight to the GPU.

All built-in geometries extend `BufferGeometry`. The old `Geometry` class was removed years ago (r125), so if you see `THREE.Geometry` in a tutorial, the tutorial is outdated.

## 11: What are the most common materials and how are they different?

- **MeshBasicMaterial**: not affected by light. Good for flat colors, wireframes and UI.
- **MeshLambertMaterial**: cheap diffuse lighting, no shiny highlights.
- **MeshPhongMaterial**: adds specular highlights. Cheap and still used for simple scenes.
- **MeshStandardMaterial**: physically based (PBR) with `roughness` and `metalness`. The usual default for realistic scenes.
- **MeshPhysicalMaterial**: extends Standard with clearcoat, transmission (glass), sheen, iridescence and more. The most expensive.
- **MeshNormalMaterial**: colors the surface based on normals. Useful for debugging.

## 12: Why does my object render completely black?

Usually because the material reacts to light and there is no light in the scene. `MeshStandardMaterial`, `MeshLambertMaterial` and `MeshPhongMaterial` all need light. Add a light or an environment map:

```js
scene.add(new THREE.AmbientLight(0xffffff, 0.5));

const sun = new THREE.DirectionalLight(0xffffff, 2);
sun.position.set(5, 10, 5);
scene.add(sun);
```

Other causes: a `MeshStandardMaterial` with `metalness: 1` and no environment map (metals reflect their surroundings, so with nothing to reflect they look black), or broken normals on a custom geometry.

## 13: What types of lights are there?

- **AmbientLight**: lights everything equally from all directions. No shadows.
- **HemisphereLight**: a sky color from above and a ground color from below. Good cheap outdoor fill light.
- **DirectionalLight**: parallel rays, like the sun. Can cast shadows.
- **PointLight**: shines in all directions from one point, like a light bulb. Can cast shadows.
- **SpotLight**: a cone of light, like a flashlight. Can cast shadows.
- **RectAreaLight**: light from a rectangle, like a window or softbox. Works only with Standard and Physical materials and doesn't cast shadows.

## 14: How do you create an animation loop?

The recommended way is `renderer.setAnimationLoop()`:

```js
renderer.setAnimationLoop((time) => {
  mesh.rotation.x = time / 1000;
  renderer.render(scene, camera);
});
```

It works like `requestAnimationFrame` but it also works in WebXR, where the browser controls the frame timing, and it is required by `WebGPURenderer`. To stop the loop, call `renderer.setAnimationLoop(null)`.

## 15: How do you move, rotate and scale an object?

Every `Object3D` has `position`, `rotation` and `scale`:

```js
mesh.position.set(0, 1, -2);
mesh.rotation.y = Math.PI / 4; // radians
mesh.scale.set(2, 2, 2);

mesh.position.x += 0.5;
mesh.translateZ(1); // move along the object's own Z axis
```

Rotations are in radians, not degrees. These values are relative to the object's parent, not the world.

## 16: What is Object3D and what is the scene graph?

`Object3D` is the base class for almost everything you put in a scene: meshes, lights, cameras, groups and the scene itself. It holds the position, rotation, scale and a list of children.

The scene graph is the tree formed by parents and children. When you move a parent, all its children move with it. `THREE.Group` is an empty `Object3D` used just to group things:

```js
const car = new THREE.Group();
car.add(body, wheel1, wheel2, wheel3, wheel4);
scene.add(car);

car.position.x = 5; // the body and the wheels all move together
```

## 17: How do you handle window resizing?

You need to update the camera's aspect ratio and the renderer size:

```js
window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```

If the canvas is not full screen, use the size of its container instead, ideally with a `ResizeObserver`, and pass `false` as the third argument of `setSize` if CSS controls the canvas size.

## 18: What does renderer.setPixelRatio do?

It tells the renderer how many real screen pixels to use per CSS pixel. On high-DPI screens (`devicePixelRatio` of 2 or 3), setting it makes the image sharp instead of blurry.

```js
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
```

Capping it at 2 is a common practice. A ratio of 3 means rendering 9 times more pixels than at ratio 1, which can kill performance on phones, and most people can't see the difference.

## 19: How do you load and apply a texture?

```js
const loader = new THREE.TextureLoader();
const texture = loader.load("/textures/wood.jpg");
texture.colorSpace = THREE.SRGBColorSpace;

const material = new THREE.MeshStandardMaterial({ map: texture });
```

`load` returns the texture right away and fills it in when the image arrives. There is also `loadAsync` that returns a promise. Set `colorSpace` to `SRGBColorSpace` for textures that hold colors (`map`, `emissiveMap`). Leave it as is for data textures like normal or roughness maps.

## 20: What are OrbitControls?

`OrbitControls` let the user rotate the camera around a target with the mouse or touch, zoom with the wheel and pan with the right button.

```js
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.target.set(0, 1, 0);

renderer.setAnimationLoop(() => {
  controls.update(); // needed when damping or autoRotate is on
  renderer.render(scene, camera);
});
```

Other controls in the addons include `MapControls`, `TrackballControls`, `FlyControls`, `PointerLockControls` and `TransformControls`.

## 21: How do you load a 3D model?

The most common way is to load a glTF file with `GLTFLoader`:

```js
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

const loader = new GLTFLoader();
const gltf = await loader.loadAsync("/models/robot.glb");
scene.add(gltf.scene);
```

The result has `gltf.scene` (the objects), `gltf.animations` (animation clips) and `gltf.cameras`. There are also loaders for OBJ, FBX, STL, PLY, USDZ and others in the addons.

## 22: Why is glTF the recommended model format?

glTF is an open standard made for delivering 3D content at runtime. It is compact, fast to parse and supports meshes, PBR materials, textures, skeletons, animations, morph targets and scene hierarchy. The `.glb` version packs everything into one binary file.

Its material model matches Three.js PBR materials closely, so models look the same as in tools like Blender. It also supports compression extensions (Draco, Meshopt, KTX2). Formats like OBJ lack animations and proper materials, and FBX is closed and heavy.

## 23: What coordinate system does Three.js use?

A right-handed coordinate system: X points right, Y points up and Z points toward the viewer (out of the screen). A camera looks down its negative Z axis by default.

There are no fixed units, but the convention is that 1 unit equals 1 meter. Following it matters because physics libraries, glTF files, WebXR and the physically based lights all assume meters.

## 24: How do you convert degrees to radians?

Use `THREE.MathUtils`:

```js
mesh.rotation.y = THREE.MathUtils.degToRad(90);
const degrees = THREE.MathUtils.radToDeg(Math.PI); // 180
```

`MathUtils` also has helpers like `clamp`, `lerp`, `damp`, `mapLinear`, `randFloat` and `smoothstep`.

## 25: What helpers does Three.js provide for debugging?

Helpers are objects that draw extra lines to show you what is going on:

```js
scene.add(new THREE.AxesHelper(2)); // red = X, green = Y, blue = Z
scene.add(new THREE.GridHelper(10, 10));
scene.add(new THREE.DirectionalLightHelper(sun));
scene.add(new THREE.CameraHelper(sun.shadow.camera));
scene.add(new THREE.BoxHelper(mesh));
```

Others include `SpotLightHelper`, `PointLightHelper`, `HemisphereLightHelper`, `ArrowHelper` and `SkeletonHelper`. `CameraHelper` on a shadow camera is very useful when shadows are cut off.

## 26: How do you add fog?

```js
scene.fog = new THREE.Fog(0xcccccc, 10, 50); // color, near, far
// or
scene.fog = new THREE.FogExp2(0xcccccc, 0.05); // color, density
```

`Fog` grows linearly between `near` and `far`. `FogExp2` grows exponentially with distance, which looks more natural. Set `scene.background` to the same color so far objects fade into the background. Materials can opt out with `fog: false`.

## 27: How do you set the background of a scene?

```js
scene.background = new THREE.Color(0x202020);
// or a texture
scene.background = texture;
// or a cube map or equirectangular HDR environment
```

If you want a transparent canvas so the HTML behind it shows through, create the renderer with `alpha: true` and leave `scene.background` as `null`.

## 28: What is Vector3 and what can you do with it?

`Vector3` holds three numbers (x, y, z). It is used for positions, directions, scales and velocities.

```js
const a = new THREE.Vector3(1, 2, 3);
const b = new THREE.Vector3(4, 5, 6);

a.add(b); // a is now (5, 7, 9)
const dist = a.distanceTo(b);
const dir = b.clone().sub(a).normalize();
const dot = a.dot(b);
a.lerp(b, 0.5);
```

Most methods change the vector in place and return `this`, so use `clone()` when you need to keep the original. There are also `Vector2`, `Vector4`, `Quaternion`, `Matrix3`, `Matrix4` and `Euler`.

## 29: How do you get rid of jagged edges?

Pass `antialias: true` when creating the renderer:

```js
const renderer = new THREE.WebGLRenderer({ antialias: true });
```

This turns on MSAA for the default framebuffer. It must be set at creation; you can't toggle it later. A higher pixel ratio also reduces jagged edges. When you use post-processing, the default framebuffer's MSAA doesn't apply to the render targets, so you need to set `samples` on the render target or add an FXAA/SMAA pass.

## 30: How are Three.js versions numbered?

Three.js uses release numbers like r186. The npm package maps that to `0.186.0`. A new release comes out regularly, and any release can contain breaking changes, because the project doesn't follow semantic versioning.

That's why you should pin the exact version in `package.json` and read the migration guide on the Three.js GitHub wiki before upgrading. Code snippets you find online often use APIs that were renamed or removed in later releases.

# Moderate Questions (31-60)

## 31: How do you detect which object the user clicked on?

Use a `Raycaster`. You convert the mouse position to normalized device coordinates (-1 to 1), shoot a ray from the camera through that point and check what it hits.

```js
const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();

renderer.domElement.addEventListener("pointerdown", (event) => {
  const rect = renderer.domElement.getBoundingClientRect();
  pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

  raycaster.setFromCamera(pointer, camera);
  const hits = raycaster.intersectObjects(clickableObjects, true);

  if (hits.length > 0) {
    console.log(hits[0].object, hits[0].point);
  }
});
```

Results are sorted by distance, so `hits[0]` is the closest. Pass only the objects you care about instead of `scene.children` to keep it fast.

## 32: Why should animations use delta time instead of a fixed step per frame?

If you do `mesh.rotation.y += 0.01` every frame, the object spins twice as fast on a 120 Hz screen as on a 60 Hz one, and it slows down when frames drop. Multiplying by the time since the last frame makes the speed the same everywhere.

```js
const timer = new THREE.Timer();
timer.connect(document); // pauses correctly when the tab is hidden

renderer.setAnimationLoop((timestamp) => {
  timer.update(timestamp);
  const delta = timer.getDelta(); // seconds

  mesh.rotation.y += 1.5 * delta; // 1.5 radians per second
  renderer.render(scene, camera);
});
```

Older code uses `THREE.Clock` for this. `Clock` is deprecated since r183. `Timer` replaces it and handles tab switching better, since `Clock` returns one huge delta after the tab comes back.

## 33: How do you play animations from a glTF model?

Use an `AnimationMixer`. Each clip from `gltf.animations` becomes an `AnimationAction` that you can play, pause, fade and loop.

```js
const gltf = await loader.loadAsync("/models/character.glb");
scene.add(gltf.scene);

const mixer = new THREE.AnimationMixer(gltf.scene);
const walk = mixer.clipAction(
  THREE.AnimationClip.findByName(gltf.animations, "Walk"),
);
const run = mixer.clipAction(
  THREE.AnimationClip.findByName(gltf.animations, "Run"),
);
walk.play();

// later, blend smoothly from walk to run
run.reset().play();
walk.crossFadeTo(run, 0.3, false);

renderer.setAnimationLoop((t) => {
  timer.update(t);
  mixer.update(timer.getDelta());
  renderer.render(scene, camera);
});
```

If you forget `mixer.update(delta)`, nothing moves.

## 34: How do you enable shadows?

Shadows are off by default and need four steps:

```js
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFShadowMap;

sun.castShadow = true;
sun.shadow.mapSize.set(2048, 2048);
sun.shadow.camera.left = -10;
sun.shadow.camera.right = 10;
sun.shadow.camera.top = 10;
sun.shadow.camera.bottom = -10;

cube.castShadow = true;
ground.receiveShadow = true;
```

Only Directional, Point and Spot lights cast shadows. For a directional light, keep the shadow camera box as small as possible around the area you need, otherwise the shadow gets blurry and blocky. `PCFSoftShadowMap` has been removed in recent releases (it falls back to `PCFShadowMap` with a warning). For softer edges use `PCFShadowMap` with `shadow.radius`, or `VSMShadowMap`.

## 35: What are the main properties of MeshStandardMaterial?

- `color` and `map`: base color.
- `roughness` / `roughnessMap`: 0 is mirror-like, 1 is fully matte.
- `metalness` / `metalnessMap`: 0 for non-metals (wood, plastic), 1 for metals. Real materials are almost always 0 or 1.
- `normalMap`: fakes small surface details without extra geometry.
- `aoMap`: ambient occlusion, darkens creases.
- `emissive`, `emissiveMap`, `emissiveIntensity`: parts that glow.
- `envMap` / `envMapIntensity`: reflections. If not set, `scene.environment` is used.
- `displacementMap`: actually moves vertices, needs enough geometry segments.

Since glTF stores roughness and metalness in one texture (green and blue channels), the same texture is often used for both maps.

## 36: How do you add realistic lighting with an HDR environment map?

Load an HDR image and assign it to `scene.environment`. All PBR materials will use it for reflections and soft ambient light.

```js
import { HDRLoader } from "three/addons/loaders/HDRLoader.js";

const envMap = await new HDRLoader().loadAsync("/env/studio.hdr");
envMap.mapping = THREE.EquirectangularReflectionMapping;

scene.environment = envMap;
scene.background = envMap; // optional
scene.backgroundBlurriness = 0.3; // optional
```

Three.js converts the map into a prefiltered format (PMREM) internally so rough materials get blurry reflections. `HDRLoader` used to be called `RGBELoader` in older versions. For product viewers, `RoomEnvironment` from the addons gives a nice studio light without loading any file.

## 37: What is color management and tone mapping in Three.js?

Lighting math must be done in linear color space, but screens expect sRGB. Three.js handles this:

- `THREE.ColorManagement.enabled` is `true` by default, so colors you pass like `0xff8800` are treated as sRGB and converted to linear.
- `renderer.outputColorSpace` is `SRGBColorSpace` by default, so the final image is converted back for display.
- Color textures must have `texture.colorSpace = THREE.SRGBColorSpace`. Data textures (normal, roughness, metalness, AO) must not. `GLTFLoader` sets this for you.

Tone mapping squeezes very bright HDR values into the 0-1 range the screen can show, instead of just clipping them to white:

```js
renderer.toneMapping = THREE.ACESFilmicToneMapping; // or AgXToneMapping, NeutralToneMapping
renderer.toneMappingExposure = 1.0;
```

Getting these wrong is the main reason scenes look washed out or too dark.

## 38: What are the common texture settings you need to know?

```js
texture.wrapS = THREE.RepeatWrapping;
texture.wrapT = THREE.RepeatWrapping;
texture.repeat.set(4, 4); // tile 4 times
texture.offset.set(0.5, 0);
texture.rotation = Math.PI / 4;
texture.anisotropy = renderer.capabilities.getMaxAnisotropy();
texture.minFilter = THREE.LinearMipmapLinearFilter;
texture.magFilter = THREE.LinearFilter;
texture.flipY = false;
```

- **wrapS/wrapT**: what happens outside 0-1 UVs (clamp, repeat, mirror).
- **anisotropy**: makes textures on surfaces seen at an angle (like floors) much sharper.
- **minFilter/magFilter**: how pixels are sampled when the texture is shrunk or enlarged. Use `NearestFilter` for pixel art.
- **flipY**: glTF textures use `flipY = false`, `TextureLoader` defaults to `true`.

If you change wrapping or image data after the texture was first used, set `texture.needsUpdate = true`.

## 39: How do you free GPU memory in Three.js?

Removing an object from the scene doesn't free its GPU resources. You must call `dispose()` on geometries, materials and textures you no longer need.

```js
function disposeObject(root) {
  root.traverse((obj) => {
    if (!obj.isMesh) return;
    obj.geometry.dispose();

    const materials = Array.isArray(obj.material)
      ? obj.material
      : [obj.material];
    for (const material of materials) {
      for (const value of Object.values(material)) {
        if (value?.isTexture) value.dispose();
      }
      material.dispose();
    }
  });
  root.removeFromParent();
}
```

Be careful with shared resources: if two meshes share a material, disposing it for one breaks the other (it will be re-uploaded the next time it renders). Render targets, `PMREMGenerator` and controls also have `dispose()`. Check `renderer.info.memory` to confirm the counts go down.

## 40: What is InstancedMesh and when should you use it?

`InstancedMesh` draws many copies of the same geometry and material in one draw call, each with its own transform and optionally its own color. It is the go-to choice for trees, grass, particles, crowds or thousands of cubes.

```js
const count = 10000;
const mesh = new THREE.InstancedMesh(geometry, material, count);
const dummy = new THREE.Object3D();
const color = new THREE.Color();

for (let i = 0; i < count; i++) {
  dummy.position.set(Math.random() * 100, 0, Math.random() * 100);
  dummy.rotation.y = Math.random() * Math.PI * 2;
  dummy.updateMatrix();
  mesh.setMatrixAt(i, dummy.matrix);
  mesh.setColorAt(i, color.setHSL(Math.random(), 0.6, 0.5));
}

mesh.instanceMatrix.needsUpdate = true;
mesh.instanceColor.needsUpdate = true;
mesh.computeBoundingSphere();
scene.add(mesh);
```

10,000 separate meshes would be 10,000 draw calls; this is one. Raycasting returns `instanceId` so you know which copy was hit. Call `computeBoundingSphere()` after moving instances, otherwise frustum culling and raycasting use the old bounds.

## 41: What is a draw call and how do you reduce them?

A draw call is one command from the CPU telling the GPU to draw something. In Three.js, roughly every visible mesh-material pair is one draw call (more with shadows and multi-material meshes). Each call has CPU overhead, so a scene with 5,000 small meshes can be slow even if the total triangle count is low.

Ways to reduce them:

- `InstancedMesh` for many copies of the same object.
- `BatchedMesh` for many different geometries that share one material.
- Merge static geometry with `BufferGeometryUtils.mergeGeometries()`.
- Share materials and use texture atlases so objects can be merged.
- Hide objects that aren't needed instead of drawing them.

```js
import { mergeGeometries } from "three/addons/utils/BufferGeometryUtils.js";
const merged = mergeGeometries(geometries);
```

You can see the count in `renderer.info.render.calls`.

## 42: How do you monitor performance in a Three.js app?

- `renderer.info` shows draw calls, triangles, number of geometries, textures and shader programs. Reset it per frame if you render multiple passes (`renderer.info.autoReset`).
- `stats.js` (in the addons as `Stats`) shows FPS and frame time.
- Chrome DevTools Performance panel shows if the CPU side (JS, matrix updates, raycasting) is the bottleneck.
- Spector.js captures a single WebGL frame and lists every GPU call, which is great for finding unexpected draw calls or state changes.

```js
console.log(renderer.info.render.calls, renderer.info.render.triangles);
console.log(renderer.info.memory.geometries, renderer.info.memory.textures);
```

## 43: How do you create a custom geometry?

Create a `BufferGeometry` and add attributes from typed arrays:

```js
const geometry = new THREE.BufferGeometry();

const positions = new Float32Array([-1, -1, 0, 1, -1, 0, 1, 1, 0, -1, 1, 0]);
const uvs = new Float32Array([0, 0, 1, 0, 1, 1, 0, 1]);

geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
geometry.setAttribute("uv", new THREE.BufferAttribute(uvs, 2));
geometry.setIndex([0, 1, 2, 0, 2, 3]);
geometry.computeVertexNormals();
```

The second argument of `BufferAttribute` is how many numbers make one vertex value (3 for positions, 2 for UVs). The index lets vertices be reused between triangles. Triangles are counter-clockwise when seen from the front. If you change positions later, set `geometry.attributes.position.needsUpdate = true`.

## 44: What is the difference between ShaderMaterial and RawShaderMaterial?

Both let you write your own GLSL shaders.

- **ShaderMaterial** adds built-in uniforms and attributes for you (`projectionMatrix`, `modelViewMatrix`, `position`, `uv`, `normal` and so on) and supports includes like `#include <fog_fragment>`.
- **RawShaderMaterial** adds nothing. You declare everything yourself, including the precision and `#version`.

```js
const material = new THREE.ShaderMaterial({
  uniforms: {
    uTime: { value: 0 },
    uColor: { value: new THREE.Color("hotpink") },
  },
  vertexShader: /* glsl */ `
    uniform float uTime;
    varying vec2 vUv;
    void main() {
      vUv = uv;
      vec3 p = position;
      p.z += sin(p.x * 4.0 + uTime) * 0.1;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(p, 1.0);
    }
  `,
  fragmentShader: /* glsl */ `
    uniform vec3 uColor;
    varying vec2 vUv;
    void main() {
      gl_FragColor = vec4(uColor * vUv.y, 1.0);
    }
  `,
});

// in the loop
material.uniforms.uTime.value = timer.getElapsed();
```

These only work with `WebGLRenderer`. With `WebGPURenderer` you write shaders in TSL instead.

## 45: How do you change a built-in material's shader without rewriting it?

Use `onBeforeCompile`. It gives you the shader source before it is compiled, so you can replace parts of it and keep all the built-in lighting, shadows and fog.

```js
const material = new THREE.MeshStandardMaterial({ color: "teal" });
const uniforms = { uTime: { value: 0 } };

material.onBeforeCompile = (shader) => {
  shader.uniforms.uTime = uniforms.uTime;
  shader.vertexShader = shader.vertexShader
    .replace("#include <common>", "#include <common>\nuniform float uTime;")
    .replace(
      "#include <begin_vertex>",
      "#include <begin_vertex>\ntransformed.y += sin(position.x * 3.0 + uTime) * 0.2;",
    );
};
```

It is a string-replace hack, so it can break when the internal shader chunks change between releases. If two materials use different code in `onBeforeCompile`, implement `customProgramCacheKey()` so they don't share the same compiled program. With `WebGPURenderer`, node materials replace this approach (for example `material.positionNode`).

## 46: How do you add post-processing effects like bloom?

With `WebGLRenderer`, use `EffectComposer` from the addons. You render the scene into a render target and then run full-screen passes over it.

```js
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { OutputPass } from "three/addons/postprocessing/OutputPass.js";

const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));
composer.addPass(
  new UnrealBloomPass(
    new THREE.Vector2(innerWidth, innerHeight),
    1.0,
    0.4,
    0.85,
  ),
);
composer.addPass(new OutputPass());

renderer.setAnimationLoop(() => composer.render());
```

`OutputPass` goes last and does tone mapping and the sRGB conversion. Remember to call `composer.setSize()` on resize. The `postprocessing` library from pmndrs is a popular alternative that merges effects into fewer passes. With `WebGPURenderer`, post-processing is built from TSL nodes with `RenderPipeline` (called `PostProcessing` before r183).

## 47: What is a render target and what can you do with it?

A render target (`WebGLRenderTarget`, or `RenderTarget` with WebGPU) is an off-screen texture you can render into instead of the canvas. You then use its texture somewhere else.

```js
const rt = new THREE.WebGLRenderTarget(512, 512);

renderer.setRenderTarget(rt);
renderer.render(otherScene, otherCamera);
renderer.setRenderTarget(null); // back to the canvas

screenMesh.material.map = rt.texture;
renderer.render(scene, camera);
```

Uses: security camera screens, mirrors and portals, minimaps, post-processing, GPU picking and reading pixels back with `readRenderTargetPixelsAsync`. Set `samples: 4` in the options for antialiasing inside the target.

## 48: Why do transparent objects look wrong, and how do you fix it?

Three.js draws opaque objects first, then transparent ones sorted from back to front by object center. Sorting is per object, not per triangle, so overlapping or intersecting transparent objects, or a single mesh that overlaps itself, can render in the wrong order.

Fixes, depending on the case:

- `depthWrite: false` on transparent materials so they don't hide each other.
- `renderOrder` to force the draw order manually.
- `alphaTest: 0.5` for cut-out textures like leaves or fences. Pixels below the threshold are discarded and the material can stay opaque, so sorting is not an issue.
- `side: THREE.DoubleSide` with transparency can show back faces in the wrong order; splitting into two meshes (back side and front side) helps.
- `alphaHash: true` gives a noisy but order-independent result.

## 49: What is the difference between local and world coordinates?

`object.position` is relative to the parent. If the object is inside a moved or rotated group, that is not its position in the world.

```js
const worldPos = new THREE.Vector3();
mesh.getWorldPosition(worldPos);

const worldQuat = new THREE.Quaternion();
mesh.getWorldQuaternion(worldQuat);

// convert a point between spaces
const local = mesh.worldToLocal(worldPoint.clone());
const world = mesh.localToWorld(new THREE.Vector3(0, 1, 0));
```

To move an object to a new parent without it jumping visually, use `newParent.attach(object)` instead of `newParent.add(object)`. `attach` keeps the world transform, `add` keeps the local one.

## 50: Why are quaternions used for rotation instead of Euler angles?

Euler angles (`rotation.x/y/z`) are easy to read, but they suffer from gimbal lock (two axes line up and you lose one degree of freedom), the result depends on the rotation order, and interpolating between two Euler rotations gives strange paths.

Quaternions don't have these problems and interpolate smoothly. Every `Object3D` keeps `rotation` and `quaternion` in sync, so you can use either one.

```js
const target = new THREE.Quaternion().setFromAxisAngle(
  new THREE.Vector3(0, 1, 0),
  Math.PI,
);

// smoothly rotate towards target
mesh.quaternion.slerp(target, 0.1);
// or with a fixed angular speed
mesh.quaternion.rotateTowards(target, 2 * delta);
```

`object.lookAt(x, y, z)` is also a simple way to point an object at something.

## 51: How do you make glTF models smaller and faster to load?

- **Draco** or **Meshopt** to compress geometry. Meshopt decodes faster and also compresses animations.
- **KTX2 (Basis Universal)** for textures. They stay compressed in GPU memory, unlike PNG and JPG which expand to full RGBA.
- Resize textures to what you really need (a 4K texture on a small object is a waste).
- Remove unused nodes, materials and animation tracks, and merge meshes where possible.

The `gltf-transform` CLI does most of this in one command. In Three.js you register the decoders:

```js
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { DRACOLoader } from "three/addons/loaders/DRACOLoader.js";
import { KTX2Loader } from "three/addons/loaders/KTX2Loader.js";
import { MeshoptDecoder } from "three/addons/libs/meshopt_decoder.module.js";

const draco = new DRACOLoader().setDecoderPath("/draco/");
const ktx2 = new KTX2Loader()
  .setTranscoderPath("/basis/")
  .detectSupport(renderer);

const loader = new GLTFLoader()
  .setDRACOLoader(draco)
  .setKTX2Loader(ktx2)
  .setMeshoptDecoder(MeshoptDecoder);
```

The decoder files are in `node_modules/three/examples/jsm/libs/draco/` and `.../libs/basis/`; copy them to your public folder.

## 52: How do you show a loading progress bar?

Use a `LoadingManager` and pass it to your loaders:

```js
const manager = new THREE.LoadingManager();

manager.onProgress = (url, loaded, total) => {
  progressBar.style.width = `${(loaded / total) * 100}%`;
};
manager.onLoad = () => loadingScreen.remove();
manager.onError = (url) => console.error("Failed to load", url);

const gltfLoader = new GLTFLoader(manager);
const textureLoader = new THREE.TextureLoader(manager);
```

The progress is counted per file, not per byte, so one large file shows 0% until it finishes. For byte-level progress of a single big file, use the `onProgress` callback of `loader.load()`.

## 53: What is React Three Fiber?

React Three Fiber (R3F) is a React renderer for Three.js. You describe the scene with JSX, and it creates and updates the Three.js objects for you. Everything in Three.js is available, it is not a wrapper with a limited API.

```jsx
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { useRef } from "react";

function Box() {
  const ref = useRef();
  useFrame((state, delta) => (ref.current.rotation.y += delta));
  return (
    <mesh ref={ref}>
      <boxGeometry />
      <meshStandardMaterial color="orange" />
    </mesh>
  );
}

export default function App() {
  return (
    <Canvas camera={{ position: [0, 0, 3] }}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[2, 2, 2]} />
      <Box />
      <OrbitControls />
    </Canvas>
  );
}
```

`@react-three/drei` adds many ready helpers (controls, loaders, text, environment). A common mistake is putting per-frame changes into React state; you should mutate refs inside `useFrame` instead, so React doesn't re-render 60 times a second.

## 54: How do you show HTML labels attached to 3D objects?

Use `CSS2DRenderer` from the addons. It positions normal HTML elements over the canvas so they follow 3D objects.

```js
import {
  CSS2DRenderer,
  CSS2DObject,
} from "three/addons/renderers/CSS2DRenderer.js";

const labelRenderer = new CSS2DRenderer();
labelRenderer.setSize(innerWidth, innerHeight);
labelRenderer.domElement.style.position = "absolute";
labelRenderer.domElement.style.top = "0";
labelRenderer.domElement.style.pointerEvents = "none";
document.body.appendChild(labelRenderer.domElement);

const div = document.createElement("div");
div.textContent = "Engine";
const label = new CSS2DObject(div);
label.position.set(0, 1.2, 0);
car.add(label);

// in the loop
renderer.render(scene, camera);
labelRenderer.render(scene, camera);
```

The labels are always on top and keep their size, and you get real text, CSS and accessibility. `CSS3DRenderer` also rotates and scales elements in 3D. For text inside the 3D scene itself, use sprites, a canvas texture or a library like `troika-three-text`.

## 55: What are layers and what can you use them for?

Every object and camera has a `layers` property with 32 layers. An object is rendered only if it shares at least one enabled layer with the camera. Raycasters have layers too.

```js
const HIDDEN_FROM_MAIN = 1;
helper.layers.set(HIDDEN_FROM_MAIN); // only on layer 1

camera.layers.enable(0); // main camera sees layer 0 only
debugCamera.layers.enable(HIDDEN_FROM_MAIN);

raycaster.layers.set(2); // only pick objects on layer 2
```

Uses: selective bloom, hiding objects from certain cameras (minimap, mirrors), and limiting raycasting to clickable objects. Lights don't use layers to decide what they light.

## 56: Why does LineBasicMaterial ignore linewidth?

WebGL lines are drawn with `gl.LINES`, and most platforms (including Chrome on Windows through ANGLE, and all WebGPU implementations) only support a line width of 1 pixel. Three.js passes the value, but the browser ignores it.

For thick lines use `Line2` with `LineMaterial` and `LineGeometry` from the addons. They build each segment out of triangles:

```js
import { Line2 } from "three/addons/lines/Line2.js";
import { LineMaterial } from "three/addons/lines/LineMaterial.js";
import { LineGeometry } from "three/addons/lines/LineGeometry.js";

const geometry = new LineGeometry().setPositions([0, 0, 0, 1, 1, 0, 2, 0, 0]);
const material = new LineMaterial({ color: 0xff0000, linewidth: 4 }); // in pixels
const line = new Line2(geometry, material);
scene.add(line);
```

Another option is building a tube mesh with `TubeGeometry`.

## 57: What is frustum culling and when can it cause problems?

Before drawing, Three.js checks each object's bounding sphere against the camera frustum (the visible pyramid). Objects completely outside are skipped. This is on by default (`object.frustumCulled = true`).

Problems appear when the bounding sphere doesn't match what is drawn:

- A shader moves vertices far from their original positions, so the object disappears at screen edges.
- Instances or vertices were changed but the bounding sphere wasn't recomputed.
- Skinned meshes whose animation moves far from the bind pose.

Fix it with `geometry.computeBoundingSphere()` after changes, by setting a bigger bounding sphere manually, or with `frustumCulled = false` as a last resort.

## 58: What is z-fighting and how do you fix it?

Z-fighting is flickering where two surfaces are at the same or almost the same depth. The depth buffer can't decide which one is in front, so they keep swapping as the camera moves.

Fixes:

- Move one surface slightly away from the other.
- Increase `camera.near` and decrease `camera.far`. A near value of `0.0001` destroys depth precision; `0.1` is usually fine.
- Use `polygonOffset` on the material for decals and overlays:

```js
const decalMaterial = new THREE.MeshStandardMaterial({
  polygonOffset: true,
  polygonOffsetFactor: -1,
  polygonOffsetUnits: -1,
});
```

- For huge scenes, use `logarithmicDepthBuffer: true` or `reversedDepthBuffer: true` on the renderer.

## 59: What tools do you use to debug a Three.js scene?

- **lil-gui** (included in the addons) to tweak positions, colors, light intensities and uniforms live.
- **Helpers** like `AxesHelper`, `CameraHelper` and `BoxHelper`.
- **The Three.js editor** (threejs.org/editor) to drop a glTF in and inspect its structure and materials.
- **Spector.js** to capture a frame and inspect every WebGL call and shader.
- **renderer.info** and **stats.js** for performance numbers.
- **gltf.report** or the glTF Viewer to check model size, textures and extensions.
- **Three.js DevTools browser extension** to inspect the scene graph.
- `MeshNormalMaterial` or `wireframe: true` to check if geometry and normals are correct.

## 60: What are morph targets?

Morph targets (blend shapes) store alternate vertex positions for the same mesh. You blend between them with weights from 0 to 1. They are used for facial expressions, lip sync and shape changes that bones can't do well.

```js
const head = gltf.scene.getObjectByName("Head");
const index = head.morphTargetDictionary["smile"];
head.morphTargetInfluences[index] = 0.8;
```

Morph targets from glTF can be animated with `AnimationMixer` like any other track. They take extra memory per target and are applied on the GPU.

# Advanced Questions (61-90)

## 61: What is WebGPURenderer and how is it different from WebGLRenderer?

`WebGPURenderer` is the newer renderer. Despite the name, it has two backends: it uses WebGPU when the browser supports it and falls back to a WebGL 2 backend otherwise, so the same code runs in both cases.

```js
import * as THREE from "three/webgpu";

const renderer = new THREE.WebGPURenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);

renderer.setAnimationLoop(() => renderer.render(scene, camera));
```

Main differences:

- Materials are node materials. Shaders are written in TSL (Three Shading Language), which compiles to WGSL or GLSL. `ShaderMaterial`, `RawShaderMaterial` and `onBeforeCompile` don't work with it.
- It supports compute shaders and storage buffers on the WebGPU backend.
- Post-processing is done with `RenderPipeline` and TSL nodes, not `EffectComposer`.
- Initialization is async. `setAnimationLoop` handles it for you, otherwise call `await renderer.init()` before the first render.

`WebGLRenderer` is still maintained and is the safer choice for projects that depend on custom GLSL or on libraries built for it. For new projects that need compute or want to be future proof, `WebGPURenderer` is the direction the project is going.

## 62: What is TSL and why was it introduced?

TSL (Three Shading Language) is a way to write shaders as JavaScript function calls instead of GLSL strings. You build a node graph, and Three.js compiles it to WGSL for WebGPU or GLSL for the WebGL backend.

```js
import * as THREE from "three/webgpu";
import {
  color,
  positionLocal,
  normalLocal,
  sin,
  time,
  mix,
  uv,
} from "three/tsl";

const material = new THREE.MeshStandardNodeMaterial();

material.colorNode = mix(color("#1e3a8a"), color("#f97316"), uv().y);
material.positionNode = positionLocal.add(
  normalLocal.mul(sin(time.mul(2).add(positionLocal.y.mul(5))).mul(0.05)),
);
```

Why it exists:

- One shader source for two shading languages.
- You can replace just one part of a built-in material (`colorNode`, `positionNode`, `normalNode`, `roughnessNode`, `emissiveNode`) and keep the lighting, shadows and fog, without string-replacing shader chunks.
- Nodes are composable and tree-shakable, and you get autocomplete and type checking in the editor.

`Fn` lets you write reusable functions with variables, `If` and `Loop` inside TSL.

## 63: How do you run a compute shader in Three.js?

With `WebGPURenderer` and TSL. A typical case is updating thousands of particles on the GPU instead of in JavaScript.

```js
import * as THREE from "three/webgpu";
import {
  Fn,
  instancedArray,
  instanceIndex,
  deltaTime,
  vec3,
  hash,
} from "three/tsl";

const count = 100000;
const positions = instancedArray(count, "vec3");
const velocities = instancedArray(count, "vec3");

const init = Fn(() => {
  const v = velocities.element(instanceIndex);
  v.assign(
    vec3(
      hash(instanceIndex),
      hash(instanceIndex.add(1)),
      hash(instanceIndex.add(2)),
    ).sub(0.5),
  );
})().compute(count);

const update = Fn(() => {
  const p = positions.element(instanceIndex);
  const v = velocities.element(instanceIndex);
  p.addAssign(v.mul(deltaTime));
})().compute(count);

const material = new THREE.SpriteNodeMaterial({ color: 0xffffff });
material.positionNode = positions.toAttribute();
material.scaleNode = 0.02;

const particles = new THREE.Sprite(material);
particles.count = count;
particles.frustumCulled = false;
scene.add(particles);

await renderer.init();
renderer.compute(init);

renderer.setAnimationLoop(() => {
  renderer.compute(update);
  renderer.render(scene, camera);
});
```

The data never leaves the GPU, so you can simulate hundreds of thousands of particles. On the WebGL 2 fallback, compute is emulated with transform feedback and has more limits, so test both paths.

## 64: What happens inside renderer.render(scene, camera)?

Roughly, for `WebGLRenderer`:

1. **Update matrices**: `scene.updateMatrixWorld()` walks the whole tree and recalculates world matrices of objects that changed. The camera's matrices are updated too.
2. **Build the frustum** from the camera's projection and view matrices.
3. **Project the scene**: walk the tree, skip invisible objects and objects outside the frustum or on other layers, collect lights, and push renderable items into render lists: opaque, transmissive and transparent.
4. **Sort**: opaque items roughly front to back (to save fragment work) and by program/material to reduce state changes. Transparent items back to front.
5. **Shadows**: render each shadow-casting light's shadow map.
6. **Transmission pass** if any material uses `transmission`.
7. **Draw**: for each item, get or compile the shader program (cached by a key built from material type, defines, lights and other settings), set uniforms, bind buffers and textures, and issue the draw call.

Knowing this helps with performance work: CPU cost comes from steps 1, 3 and 7 (many objects), GPU cost from the draws themselves (pixels and triangles), and stutter usually comes from compiling new programs in step 7.

## 65: Why does the app freeze for a moment when a new object appears, and how do you fix it?

Most likely a shader program is being compiled. Three.js compiles a program the first time a material with a new combination of settings is rendered. Compiling a large PBR shader can take tens or hundreds of milliseconds, and it blocks the main thread.

Things that create new programs: a new material type, toggling `map`/`normalMap` on or off, changing the number of lights, enabling shadows on a light, changing `defines`, fog on/off, a different `side` in some cases.

Fixes:

- Precompile at load time with `await renderer.compileAsync(scene, camera)`. It uses the `KHR_parallel_shader_compile` extension when available so the main thread isn't blocked.
- Add hidden objects to the scene during loading so their materials compile before they are needed.
- Keep the number of lights stable. Turning a light on by setting `intensity` is cheap; adding a new light changes every lit program.
- Reuse materials instead of creating new ones with slightly different settings.
- Check `renderer.info.programs.length` to see how many programs you have.

## 66: A scene has 20,000 objects and runs at 15 FPS. How do you approach it?

First measure, then fix the bottleneck you find.

1. **Check if it's CPU or GPU bound.** Lower the pixel ratio or shrink the canvas. If FPS jumps, it is GPU fill rate. If not, it is CPU (draw calls, matrix updates, JS logic). The DevTools Performance panel confirms it.
2. **Look at `renderer.info.render.calls`.** 20,000 objects is likely close to 20,000 draw calls, which is the classic CPU bottleneck.

Fixes for CPU:

- `InstancedMesh` for repeated objects, `BatchedMesh` for different geometries with one material, or merge static meshes into a few.
- `matrixAutoUpdate = false` on static objects.
- Fewer unique materials; use atlases or vertex colors.
- Spatial structures (BVH, grids) for raycasting and game logic instead of looping over everything.

Fixes for GPU:

- Cap the pixel ratio, lower shadow map sizes, fewer shadow-casting lights.
- `LOD` to swap distant objects for simpler versions.
- Cheaper materials for distant or small objects, fewer post-processing passes.
- Compressed textures to reduce memory bandwidth.

```js
const lod = new THREE.LOD();
lod.addLevel(highDetail, 0);
lod.addLevel(mediumDetail, 30);
lod.addLevel(lowDetail, 80);
scene.add(lod);
```

## 67: When do you pick InstancedMesh, BatchedMesh or merged geometry?

- **InstancedMesh**: many copies of exactly the same geometry and material. Each copy has its own matrix and color. Cheapest option. Can't mix different shapes.
- **BatchedMesh**: many different geometries sharing one material, drawn with a single call (multi-draw). Each instance can be moved, hidden and recolored, and individual instances are frustum culled and can be sorted. Good for things like city blocks or CAD parts.
- **Merged geometry** (`mergeGeometries`): everything baked into one static buffer. Simplest and very fast to draw, but you can't move parts separately, it is culled as one object, and it can use a lot of memory if you merge many copies of the same mesh.

```js
const batched = new THREE.BatchedMesh(1000, 50000, 100000, material);
const boxId = batched.addGeometry(new THREE.BoxGeometry());
const sphereId = batched.addGeometry(new THREE.SphereGeometry(0.5, 16, 8));

const matrix = new THREE.Matrix4();
const a = batched.addInstance(boxId);
batched.setMatrixAt(a, matrix.makeTranslation(-2, 0, 0));
const b = batched.addInstance(sphereId);
batched.setMatrixAt(b, matrix.makeTranslation(2, 0, 0));

scene.add(batched);
```

The constructor arguments are max instances, max vertices and max indices, so you allocate the buffers up front.

## 68: How do you handle very large models and textures without running out of GPU memory?

GPU memory, not file size, is usually the limit. A 4096x4096 JPEG may be 2 MB on disk, but it becomes about 64 MB in GPU memory as uncompressed RGBA, plus about a third more for mipmaps.

Approaches:

- **KTX2/Basis textures**: they stay compressed on the GPU (BC on desktop, ASTC/ETC on mobile), usually 4-8 times smaller than raw RGBA.
- **Right-size textures**: 1K or 2K is enough for most objects. Pack roughness, metalness and AO into one texture's channels.
- **Geometry compression** (Meshopt, Draco) for download size, plus simplification for lower LODs (`gltf-transform simplify` or meshoptimizer).
- **Stream content**: load and dispose parts of the scene based on where the camera is, instead of loading everything at once. For huge datasets like cities or point clouds, use 3D Tiles (the `3d-tiles-renderer` library).
- **Dispose what you don't use** and verify with `renderer.info.memory`.
- On mobile, a WebGL context crash (context lost) is often the sign that you ran out of memory.

## 69: How do matrix updates work, and how can you reduce their cost?

Every `Object3D` has a local `matrix` built from `position`, `quaternion` and `scale`, and a `matrixWorld` that is the parent's world matrix times the local one. By default, each `render()` call runs `scene.updateMatrixWorld()`, which recomputes local matrices for all objects (`matrixAutoUpdate = true`) and world matrices down the tree.

With tens of thousands of objects this shows up in profiles. Ways to cut it:

```js
// static object: compute once and stop updating
building.matrixAutoUpdate = false;
building.updateMatrix();

// after you move it manually later
building.position.x = 10;
building.updateMatrix();
```

- `object.matrixWorldAutoUpdate = false` stops the renderer from updating the world matrix of that object and its subtree; you then call `updateMatrixWorld()` yourself when needed.
- Keep hierarchies shallow. Deep nesting means more multiplications per change.
- Use `InstancedMesh` or `BatchedMesh`, where one object holds many transforms.

If you read `matrixWorld` or call `getWorldPosition` before the first render or right after moving a parent, call `updateMatrixWorld()` first, otherwise you get stale values.

## 70: Raycasting against a detailed model is slow. How do you make it faster?

`Raycaster` by default tests every triangle of every mesh you pass in. Against a model with millions of triangles on every `pointermove`, it can take many milliseconds.

Options:

- **three-mesh-bvh**: builds a bounding volume hierarchy for each geometry so the ray only checks a few triangles. It is usually a 100x or bigger speedup and also gives fast shape casts and distance queries.

```js
import {
  computeBoundsTree,
  disposeBoundsTree,
  acceleratedRaycast,
} from "three-mesh-bvh";

THREE.BufferGeometry.prototype.computeBoundsTree = computeBoundsTree;
THREE.BufferGeometry.prototype.disposeBoundsTree = disposeBoundsTree;
THREE.Mesh.prototype.raycast = acceleratedRaycast;

geometry.computeBoundsTree();
raycaster.firstHitOnly = true;
```

- Raycast against simple proxy shapes (an invisible low-poly mesh or a box) instead of the visual mesh.
- Limit targets with layers or a separate array of pickable objects.
- Throttle raycasts, for example once per frame instead of on every mouse event.
- **GPU picking**: render object IDs as colors into a small render target and read the pixel under the cursor. Cost doesn't depend on triangle count, but it needs an extra render pass and an async pixel read.

## 71: How do you get good-looking shadows without killing performance?

Shadows are expensive because each shadow-casting light renders the scene again (a point light renders it 6 times, once per cube face).

Quality:

- Fit the directional light's shadow camera tightly around the visible area; a smaller area means sharper shadows from the same map size.
- Fix **shadow acne** (striped self-shadowing) with a small negative `shadow.bias` or a positive `shadow.normalBias`. Too much bias causes **peter panning**, where the shadow detaches from the object.
- For large outdoor scenes, use cascaded shadow maps (`CSM` from the addons) so close shadows are sharp and far ones are cheap.

Performance:

- Few shadow-casting lights, ideally one directional light.
- Only enable `castShadow` on objects that matter.
- For static scenes, render the shadow map once: `renderer.shadowMap.autoUpdate = false` and set `renderer.shadowMap.needsUpdate = true` when something moves.
- Bake shadows and ambient occlusion into lightmaps in Blender for static environments. This is the cheapest and often the best looking option.
- Use a fake blob shadow (a plane with a soft texture) under characters or products.

## 72: How do you deal with depth precision problems in large scenes?

The depth buffer has limited precision, and most of it is spent close to the near plane. With `near = 0.01` and `far = 100000` (planets, maps, large terrains) distant surfaces z-fight badly.

Options:

- Push `near` as far out as you can. The near-to-far ratio matters much more than `far` alone.
- `logarithmicDepthBuffer: true` spreads precision more evenly. It works everywhere but writes depth in the fragment shader, which disables early depth testing and costs some performance.
- `reversedDepthBuffer: true` (WebGL needs `EXT_clip_control`, WebGPU supports it) uses a float depth buffer with reversed range, which gives very good precision across the whole range and keeps early depth testing. Check `renderer.capabilities.reversedDepthBuffer` to see if it is active.
- Split the scene into near and far parts and render them in two passes with different camera ranges, clearing depth in between.

```js
const renderer = new THREE.WebGLRenderer({ reversedDepthBuffer: true });
```

## 73: How do you apply bloom only to some objects?

`UnrealBloomPass` blooms everything brighter than the threshold. To bloom only selected objects there are two common approaches.

**Use HDR brightness as the selector.** Render to a half-float target (EffectComposer does this by default), set the bloom threshold to 1, and give the objects you want to glow an emissive color with `emissiveIntensity` above 1. Only those pixels exceed the threshold. This is simple and works well when the rest of the scene stays below 1.

**Use a separate bloom render.** Put glowing objects on a layer, render the scene once with everything else darkened (swap their materials to black or hide them) into a bloom composer, then combine it with the normal render in a final shader pass. This is the official "selective bloom" example. It is more precise but costs an extra scene render and material swapping.

With `WebGPURenderer` it is cleaner: render the scene once with MRT, writing both `output` and `emissive`, and run `bloom()` only on the emissive output:

```js
import { pass, mrt, output, emissive } from "three/tsl";
import { bloom } from "three/addons/tsl/display/BloomNode.js";

const scenePass = pass(scene, camera);
scenePass.setMRT(mrt({ output, emissive }));

const color = scenePass.getTextureNode("output");
const glow = scenePass.getTextureNode("emissive");

const pipeline = new THREE.RenderPipeline(renderer);
pipeline.outputNode = color.add(bloom(glow, 2.5, 0.5));

renderer.setAnimationLoop(() => pipeline.render());
```

## 74: What is a lost WebGL context and how do you handle it?

The browser can take the GPU context away from a page: the GPU driver resets, the device runs out of memory, too many WebGL contexts are open (browsers allow around 16), or a mobile OS reclaims resources. The canvas goes black.

```js
const canvas = renderer.domElement;

canvas.addEventListener("webglcontextlost", (event) => {
  event.preventDefault(); // allows the context to be restored
  renderer.setAnimationLoop(null);
  showMessage("Graphics were reset, restoring...");
});

canvas.addEventListener("webglcontextrestored", () => {
  hideMessage();
  renderer.setAnimationLoop(animate);
});
```

Three.js re-initializes its internal state on restore, and it re-uploads geometries and textures as long as the source data is still in memory. Textures created from `ImageBitmap` that were closed, or data you dropped after upload, must be recreated by you. Test it with `renderer.forceContextLoss()` and `renderer.forceContextRestore()`. Avoid creating many renderers (for example one per React component) since each one takes a context.

## 75: How do you run Three.js in a Web Worker?

Transfer the canvas to a worker with `OffscreenCanvas`. Rendering and scene logic then run off the main thread, so heavy JS on the page doesn't make the 3D view stutter, and vice versa.

```js
// main.js
const canvas = document.querySelector("canvas");
const offscreen = canvas.transferControlToOffscreen();
const worker = new Worker(new URL("./render-worker.js", import.meta.url), {
  type: "module",
});

worker.postMessage(
  {
    type: "init",
    canvas: offscreen,
    width: canvas.clientWidth,
    height: canvas.clientHeight,
    dpr: devicePixelRatio,
  },
  [offscreen],
);
```

```js
// render-worker.js
import * as THREE from "three";

self.onmessage = ({ data }) => {
  if (data.type !== "init") return;
  const renderer = new THREE.WebGLRenderer({
    canvas: data.canvas,
    antialias: true,
  });
  renderer.setPixelRatio(data.dpr);
  renderer.setSize(data.width, data.height, false); // false: there is no style in a worker
  // build scene, then renderer.setAnimationLoop(...)
};
```

Limitations: no DOM in the worker, so controls like `OrbitControls` need input events forwarded from the main thread (with a fake element object). `TextureLoader` uses `Image`, which doesn't exist in workers; use `ImageBitmapLoader` instead. Resize events must also be sent manually.

## 76: How do you avoid memory leaks when using Three.js in a single-page app?

In SPAs, users navigate away from the 3D page and back many times. If you don't clean up, every visit leaks GPU memory, event listeners and sometimes a whole WebGL context.

On unmount:

```js
function destroy() {
  renderer.setAnimationLoop(null);
  controls.dispose();
  window.removeEventListener("resize", onResize);

  scene.traverse((obj) => {
    if (obj.geometry) obj.geometry.dispose();
    if (obj.material) {
      const materials = Array.isArray(obj.material)
        ? obj.material
        : [obj.material];
      materials.forEach((m) => {
        Object.values(m).forEach((v) => v?.isTexture && v.dispose());
        m.dispose();
      });
    }
  });

  scene.environment?.dispose();
  composer?.dispose();
  renderer.dispose();
  renderer.domElement.remove();
}
```

Also watch out for closures that keep the scene alive (event handlers, global caches, `THREE.Cache` if enabled), animation mixers (`mixer.stopAllAction()` and `mixer.uncacheRoot(root)`), and objects stored in state management. Confirm with `renderer.info.memory` and heap snapshots that numbers return to the baseline after navigating back and forth. React Three Fiber disposes objects it created automatically when they unmount, but not things you created manually and passed in through `object` props.

## 77: Why does cloning a glTF character break its animation, and how do you clone it correctly?

`gltf.scene.clone()` copies the objects, but the cloned `SkinnedMesh` still points to the bones of the original skeleton. Animating the clone either does nothing or moves the original.

Use `SkeletonUtils.clone`, which rebuilds the skeleton with the cloned bones:

```js
import * as SkeletonUtils from "three/addons/utils/SkeletonUtils.js";

const gltf = await loader.loadAsync("/models/soldier.glb");

for (let i = 0; i < 10; i++) {
  const soldier = SkeletonUtils.clone(gltf.scene);
  soldier.position.x = i * 2;
  scene.add(soldier);

  const mixer = new THREE.AnimationMixer(soldier);
  mixer.clipAction(gltf.animations[0]).play();
  mixers.push(mixer);
}
```

Geometry and materials are shared between clones, which saves memory. Note that each clone is still a separate set of draw calls and has its own skinning cost. For crowds of hundreds or thousands, people bake animations into textures and use instancing, or use simpler LODs for distant characters.

## 78: How would you render a million points efficiently?

Use `THREE.Points` with a single `BufferGeometry`. It is one draw call no matter how many points there are.

```js
const count = 1_000_000;
const positions = new Float32Array(count * 3);
const colors = new Float32Array(count * 3);

for (let i = 0; i < count * 3; i++) {
  positions[i] = (Math.random() - 0.5) * 100;
  colors[i] = Math.random();
}

const geometry = new THREE.BufferGeometry();
geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
geometry.setAttribute("color", new THREE.BufferAttribute(colors, 3));

const material = new THREE.PointsMaterial({
  size: 0.05,
  vertexColors: true,
  sizeAttenuation: true,
});
scene.add(new THREE.Points(geometry, material));
```

Tips:

- If the points move, animate them in the vertex shader (uniform time, or TSL with compute) instead of rewriting the array in JS every frame.
- If you must update from JS, update only the changed range with `attribute.addUpdateRange(start, count)` and set `attribute.usage = THREE.DynamicDrawUsage`.
- Avoid transparency with sorting; use additive blending with `depthWrite: false` for glowing particles.
- Raycasting a million points is slow; set `raycaster.params.Points.threshold` and use a spatial index if you need picking.
- Point size is limited by the GPU (often 64 or more pixels, but not guaranteed). For large sprites use instanced quads instead.

## 79: Objects far from the origin start shaking. Why, and how do you fix it?

This is floating-point precision loss. GPUs use 32-bit floats, which have about 7 significant digits. At coordinates like 5,000,000 (a real-world map in meters) the smallest step is around half a meter, so vertices snap between values and the model jitters as the camera moves.

Fixes:

- **Floating origin (origin rebasing)**: keep the camera near (0, 0, 0). When it moves too far, shift the whole world back by the camera's offset. You store real coordinates in double precision (JS numbers) on the CPU and only send local offsets to the GPU.
- **Relative-to-center**: store each tile's or model's vertices relative to its own center, and place the object with its `position`. Three.js computes `modelViewMatrix` on the CPU in 64-bit, so large `position` values with small local vertices are mostly fine.
- Don't bake large coordinates into vertex data. Convert geographic data into local coordinates around a reference point.

## 80: How do you make a Three.js scene run well on low-end mobile devices?

- **Pixel ratio**: cap at 1.5 or even 1 on weak devices. It is the biggest single win.
- **Adaptive quality**: measure frame time and lower the pixel ratio or turn effects off when FPS drops, raise it again when it recovers.
- **Render on demand** when nothing is moving instead of 60 FPS all the time. This also saves battery.
- **Cheaper materials**: `MeshLambertMaterial` or `MeshStandardMaterial` instead of `MeshPhysicalMaterial`; avoid `transmission`.
- **Bake lighting** into textures, avoid real-time shadows or use one small shadow map.
- **Compressed textures** (KTX2) and smaller sizes; mobile GPUs have little memory and bandwidth.
- **Skip or simplify post-processing**. Each full-screen pass at phone resolution is costly.
- `powerPreference: 'high-performance'` asks for the dedicated GPU on laptops that have two; it doesn't help much on phones.

```js
let dpr = Math.min(devicePixelRatio, 2);

function adjustQuality(frameMs) {
  if (frameMs > 22 && dpr > 1) dpr -= 0.25;
  else if (frameMs < 14 && dpr < Math.min(devicePixelRatio, 2)) dpr += 0.25;
  renderer.setPixelRatio(dpr);
}
```

## 81: How do you render only when something changes?

For product viewers, configurators and dashboards, the scene is static most of the time. Rendering 60 times a second then wastes battery and heats the device.

```js
let needsRender = true;

function requestRender() {
  needsRender = true;
}

controls.addEventListener("change", requestRender);
window.addEventListener("resize", () => {
  // update camera and renderer size...
  requestRender();
});

renderer.setAnimationLoop(() => {
  if (controls.update()) needsRender = true; // returns true when damping moved the camera
  if (!needsRender) return;
  needsRender = false;
  renderer.render(scene, camera);
});
```

Call `requestRender()` whenever you change a material, load a model or start an animation. While an `AnimationMixer` or tween is running, keep rendering every frame. React Three Fiber supports this with `<Canvas frameloop="demand">` and `invalidate()`.

## 82: What do you check when upgrading an old project to a recent Three.js version?

Read the migration guide on the GitHub wiki for every release between your version and the target. The big changes from the last few years:

- **Color management** (r152): color management is on and output is sRGB by default. Color textures need `colorSpace = SRGBColorSpace`. `outputEncoding` and `texture.encoding` were replaced by `outputColorSpace` and `texture.colorSpace`.
- **Lighting** (r155, r165): physically correct lighting is the default and `useLegacyLights` was removed. Light intensities need to be raised, often multiplied by about PI, and point/spot lights use `decay = 2` and real distances.
- **Imports**: `examples/js` (global scripts) is gone; use ES modules from `three/addons/`.
- **Removed classes**: `Geometry` (r125), `Clock` deprecated in favor of `Timer` (r183), `RGBELoader` renamed to `HDRLoader`, `PCFSoftShadowMap` removed, `PostProcessing` renamed to `RenderPipeline` for WebGPU.
- **Custom shaders**: chunk names and code used in `onBeforeCompile` change between releases, so every string replace must be checked.

Upgrade in steps rather than jumping 50 releases at once, keep the console open for deprecation warnings, and compare screenshots before and after.

## 83: How do light intensities work in physically based lighting?

Since physically correct lighting became the only mode, light values roughly follow real-world units, assuming 1 unit = 1 meter:

- `PointLight` and `SpotLight` intensity is in candela. Their brightness falls off with the inverse square of distance (`decay = 2`, the default). `distance = 0` means no cutoff.
- `DirectionalLight` and `AmbientLight` intensity is in lux-like units (irradiance), with no falloff.
- `RectAreaLight` intensity is in nits (luminance).
- `PointLight`, `SpotLight` and `RectAreaLight` also have a `power` property in lumens as an alternative to `intensity`.

In practice you combine this with an environment map, tone mapping and exposure, just like a camera. If a point light seems to do nothing, check the scene scale: a model exported in centimeters is 100 times larger than expected, so the light falls off before it reaches anything.

## 84: How do you build a WebXR (VR or AR) experience with Three.js?

Enable XR on the renderer and use the button helpers from the addons to start a session:

```js
import { VRButton } from "three/addons/webxr/VRButton.js";

renderer.xr.enabled = true;
document.body.appendChild(VRButton.createButton(renderer));

const controller = renderer.xr.getController(0);
controller.addEventListener("select", onSelect);
scene.add(controller);

renderer.setAnimationLoop(() => renderer.render(scene, camera));
```

For AR, use `ARButton` with features like `hit-test` to place objects on real surfaces. `XRControllerModelFactory` and `XRHandModelFactory` show controller and hand models.

Things that matter in XR:

- You must use `setAnimationLoop`; `requestAnimationFrame` doesn't run in an immersive session.
- The scene is rendered twice (one per eye) at 72-120 Hz, so the performance budget is much tighter than on desktop. Dropped frames make people feel sick.
- Units must be meters, and the camera is controlled by the headset; move the user by moving a parent group, not the camera.
- Avoid heavy post-processing and keep draw calls low.

## 85: How do you write your own post-processing pass with EffectComposer?

The easiest way is `ShaderPass` with a shader object. The previous pass's result comes in as the `tDiffuse` uniform.

```js
import { ShaderPass } from "three/addons/postprocessing/ShaderPass.js";

const VignetteShader = {
  uniforms: {
    tDiffuse: { value: null },
    uStrength: { value: 0.6 },
  },
  vertexShader: /* glsl */ `
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
  fragmentShader: /* glsl */ `
    uniform sampler2D tDiffuse;
    uniform float uStrength;
    varying vec2 vUv;
    void main() {
      vec4 color = texture2D(tDiffuse, vUv);
      float d = distance(vUv, vec2(0.5));
      color.rgb *= 1.0 - smoothstep(0.3, 0.8, d) * uStrength;
      gl_FragColor = color;
    }
  `,
};

const vignettePass = new ShaderPass(VignetteShader);
composer.insertPass(vignettePass, composer.passes.length - 1); // before OutputPass
```

Keep in mind that the passes work in linear HDR color until `OutputPass`, so color math must be done in linear space. For effects that need depth or normals, render them into extra targets or use the pass that provides them. Every pass is one full-screen draw, so combine simple effects into one shader when possible.

## 86: How do you add physics to a Three.js scene?

Three.js has no physics engine. You use a separate library, most often **Rapier** (Rust compiled to WASM, fast and deterministic) or **cannon-es** (pure JS, simpler). The physics world owns the simulation, and every frame you copy positions and rotations from physics bodies to the meshes.

Run physics on a fixed timestep so the result doesn't depend on the frame rate:

```js
const FIXED_STEP = 1 / 60;
let accumulator = 0;

renderer.setAnimationLoop((t) => {
  timer.update(t);
  accumulator += Math.min(timer.getDelta(), 0.1); // avoid a spiral after a long pause

  while (accumulator >= FIXED_STEP) {
    world.step(); // Rapier uses world.timestep, set it to FIXED_STEP
    accumulator -= FIXED_STEP;
  }

  for (const { mesh, body } of dynamicObjects) {
    mesh.position.copy(body.translation());
    mesh.quaternion.copy(body.rotation());
  }

  renderer.render(scene, camera);
});
```

Use simple collider shapes (boxes, spheres, capsules) instead of the visual mesh. Triangle mesh colliders are slow and should only be used for static terrain. For React Three Fiber, `@react-three/rapier` wraps all this.

## 87: Why does a texture from another domain fail to load, and how do you fix it?

WebGL can't use images from another origin unless the server allows it with CORS. Otherwise the image would let a page read pixels of cross-origin content, which is a security hole. You'll see a `SecurityError` or a CORS error in the console and the texture stays black.

Fixes:

- The server must send `Access-Control-Allow-Origin` (your domain or `*`) for the image.
- Three.js loaders request with `crossOrigin = 'anonymous'` by default. Use `loader.setCrossOrigin('use-credentials')` only if the server needs cookies.
- Or host the assets on your own domain or behind your own proxy/CDN.

Related security points: don't load models or shader code from untrusted user input without checks (huge files can freeze or crash the tab), validate URLs used in loaders, and keep the Draco/Basis decoder files self-hosted so a third-party CDN can't change the code your page runs.

## 88: How do you structure a large Three.js application?

Three.js is a rendering library, not an engine, so the structure is up to you. Things that work well in larger projects:

- **Separate the app shell from the 3D core.** One class or module owns the renderer, scene, camera and loop. UI frameworks (React, Vue, Angular) talk to it through a small API or events, not by touching meshes directly.
- **Asset manager.** One place to load, cache, reference count and dispose models and textures, so two features using the same model don't load it twice or dispose it while the other still uses it.
- **Systems that run per frame.** Instead of one huge `animate` function, register update callbacks (`animation`, `physics`, `input`, `ui`) with a clear order. An ECS library like `bitecs` or `koota` helps when you have many entities.
- **Keep state outside the scene graph.** Store app data (selected item, configuration) in your own store, and sync the scene from it. The scene should be a view of the state.
- **Plan for cleanup** from day one: every feature that adds objects should know how to remove and dispose them.
- **Pin the Three.js version** and wrap API calls that change often, so upgrades touch fewer files.

## 89: A model looks different in Three.js than in Blender. What do you check?

Go through the usual suspects:

1. **Color space**: color textures must be sRGB, data textures linear. With `GLTFLoader` this is automatic, but custom loaders or manually loaded textures often get it wrong.
2. **Tone mapping and exposure**: Blender uses AgX (or Filmic in older versions). Set `renderer.toneMapping = THREE.AgXToneMapping` to match, and adjust exposure.
3. **Lighting**: Blender scenes are often lit by an HDRI. Without `scene.environment` in Three.js, PBR materials look flat or black, especially metals.
4. **Light units**: Blender watts don't map directly to Three.js intensities. glTF export converts them, but values often need tweaking.
5. **Unsupported material nodes**: only what glTF supports is exported (Principled BSDF and some extensions). Procedural textures and custom node setups must be baked to images.
6. **Normals and backfaces**: flipped normals show as black or missing faces. Check with `MeshNormalMaterial` or `side: DoubleSide`.
7. **Scale and units**: a model exported in centimeters will be 100x too big and break lighting and shadows.

Viewing the file in an online glTF viewer helps tell whether the problem is in the export or in your Three.js setup.

## 90: How do you choose between plain Three.js, React Three Fiber and a full engine like Babylon.js or PlayCanvas?

- **Plain Three.js**: full control, smallest abstraction, good for custom visualizations, landing page effects and teams that want to own the architecture. You build the structure yourself (loop, asset management, cleanup).
- **React Three Fiber**: a good fit when the app is already React and the 3D view is part of a larger UI. You get components, hooks, automatic cleanup and the drei/rapier ecosystem. It adds a learning curve around React performance (avoid state updates per frame).
- **Babylon.js / PlayCanvas**: full engines with an inspector, physics integration, GUI system, editor (PlayCanvas) and more built in. Better for games or when the team wants a ready framework with stronger backward compatibility guarantees.

Things to weigh: team experience, how much of the app is 3D vs regular UI, need for an editor for non-developers, bundle size, long-term upgrade cost (Three.js breaks APIs more often), and the size of the community and examples. Three.js has by far the largest community and the most learning material, which matters a lot when you get stuck.
