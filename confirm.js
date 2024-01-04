function dontFuckWithMe(e) {
    e.stopImmediatePropagation()
}

document.addEventListener(
    'paste',
    dontFuckWithMe,
    true
);