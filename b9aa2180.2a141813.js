(window.webpackJsonp=window.webpackJsonp||[]).push([[28],{107:function(e,t,n){"use strict";n.d(t,"a",(function(){return p})),n.d(t,"b",(function(){return f}));var o=n(0),r=n.n(o);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,o)}return n}function c(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function u(e,t){if(null==e)return{};var n,o,r=function(e,t){if(null==e)return{};var n,o,r={},a=Object.keys(e);for(o=0;o<a.length;o++)n=a[o],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(o=0;o<a.length;o++)n=a[o],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var d=r.a.createContext({}),s=function(e){var t=r.a.useContext(d),n=t;return e&&(n="function"==typeof e?e(t):c(c({},t),e)),n},p=function(e){var t=s(e.components);return r.a.createElement(d.Provider,{value:t},e.children)},l={inlineCode:"code",wrapper:function(e){var t=e.children;return r.a.createElement(r.a.Fragment,{},t)}},m=r.a.forwardRef((function(e,t){var n=e.components,o=e.mdxType,a=e.originalType,i=e.parentName,d=u(e,["components","mdxType","originalType","parentName"]),p=s(n),m=o,f=p["".concat(i,".").concat(m)]||p[m]||l[m]||a;return n?r.a.createElement(f,c(c({ref:t},d),{},{components:n})):r.a.createElement(f,c({ref:t},d))}));function f(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var a=n.length,i=new Array(a);i[0]=m;var c={};for(var u in t)hasOwnProperty.call(t,u)&&(c[u]=t[u]);c.originalType=e,c.mdxType="string"==typeof e?e:o,i[1]=c;for(var d=2;d<a;d++)i[d]=n[d];return r.a.createElement.apply(null,i)}return r.a.createElement.apply(null,n)}m.displayName="MDXCreateElement"},94:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return i})),n.d(t,"metadata",(function(){return c})),n.d(t,"rightToc",(function(){return u})),n.d(t,"default",(function(){return s}));var o=n(3),r=n(7),a=(n(0),n(107)),i={id:"contrib-documentation-tasks",title:"Task Documentation",desc:"Provides basic information on creating documentation for ORCA tasks."},c={unversionedId:"developer/development-guide/documentation/contrib-documentation-tasks",id:"developer/development-guide/documentation/contrib-documentation-tasks",isDocsHomePage:!1,title:"Task Documentation",description:"Task documentation is created as part of the build process. Information on",source:"@site/docs/developer/development-guide/documentation/documentation-tasks.md",slug:"/developer/development-guide/documentation/contrib-documentation-tasks",permalink:"/cumulus-orca/docs/developer/development-guide/documentation/contrib-documentation-tasks",editUrl:"https://github.com/nasa/cumulus-orca/edit/develop/website/docs/developer/development-guide/documentation/documentation-tasks.md",version:"current",sidebar:"dev_guide",previous:{title:"Documentation Templates",permalink:"/cumulus-orca/docs/developer/development-guide/documentation/contrib-documentation-templates"},next:{title:"Documentation Style Guide",permalink:"/cumulus-orca/docs/developer/development-guide/documentation/documentation-style-guide"}},u=[],d={rightToc:u};function s(e){var t=e.components,n=Object(r.a)(e,["components"]);return Object(a.b)("wrapper",Object(o.a)({},d,n,{components:t,mdxType:"MDXLayout"}),Object(a.b)("p",null,"Task documentation is created as part of the build process. Information on\ntask templates and building task documentation is TBD."))}s.isMDXComponent=!0}}]);