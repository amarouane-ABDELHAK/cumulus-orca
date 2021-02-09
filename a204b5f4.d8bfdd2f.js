(window.webpackJsonp=window.webpackJsonp||[]).push([[26],{108:function(e,t,n){"use strict";n.d(t,"a",(function(){return p})),n.d(t,"b",(function(){return b}));var o=n(0),r=n.n(o);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function c(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,o)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?c(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):c(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,o,r=function(e,t){if(null==e)return{};var n,o,r={},i=Object.keys(e);for(o=0;o<i.length;o++)n=i[o],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(o=0;o<i.length;o++)n=i[o],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var u=r.a.createContext({}),d=function(e){var t=r.a.useContext(u),n=t;return e&&(n="function"==typeof e?e(t):a(a({},t),e)),n},p=function(e){var t=d(e.components);return r.a.createElement(u.Provider,{value:t},e.children)},m={inlineCode:"code",wrapper:function(e){var t=e.children;return r.a.createElement(r.a.Fragment,{},t)}},s=r.a.forwardRef((function(e,t){var n=e.components,o=e.mdxType,i=e.originalType,c=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),p=d(n),s=o,b=p["".concat(c,".").concat(s)]||p[s]||m[s]||i;return n?r.a.createElement(b,a(a({ref:t},u),{},{components:n})):r.a.createElement(b,a({ref:t},u))}));function b(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var i=n.length,c=new Array(i);c[0]=s;var a={};for(var l in t)hasOwnProperty.call(t,l)&&(a[l]=t[l]);a.originalType=e,a.mdxType="string"==typeof e?e:o,c[1]=a;for(var u=2;u<i;u++)c[u]=n[u];return r.a.createElement.apply(null,c)}return r.a.createElement.apply(null,n)}s.displayName="MDXCreateElement"},92:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return c})),n.d(t,"metadata",(function(){return a})),n.d(t,"rightToc",(function(){return l})),n.d(t,"default",(function(){return d}));var o=n(3),r=n(7),i=(n(0),n(108)),c={id:"deployment",title:"Deployment Information",description:"Provides developer information for ORCA code deployment."},a={unversionedId:"developer/deployment-guide/deployment",id:"developer/deployment-guide/deployment",isDocsHomePage:!1,title:"Deployment Information",description:"Provides developer information for ORCA code deployment.",source:"@site/docs/developer/deployment-guide/deployment.md",slug:"/developer/deployment-guide/deployment",permalink:"/cumulus-orca/docs/developer/deployment-guide/deployment",editUrl:"https://github.com/nasa/cumulus-orca/edit/develop/website/docs/developer/deployment-guide/deployment.md",version:"current",sidebar:"dev_guide",previous:{title:"Deploying Documentation",permalink:"/cumulus-orca/docs/developer/development-guide/documentation/contrib-documentation-deploy"},next:{title:"Creating a Deployment Environment",permalink:"/cumulus-orca/docs/developer/deployment-guide/deployment-environment"}},l=[{value:"Deploying ORCA",id:"deploying-orca",children:[{value:"Setup Deployment Environment",id:"setup-deployment-environment",children:[]},{value:"ORCA Archive Bucket",id:"orca-archive-bucket",children:[]},{value:"Deploy ORCA with Cumulus",id:"deploy-orca-with-cumulus",children:[]}]},{value:"Configuring ORCA",id:"configuring-orca",children:[]}],u={rightToc:l};function d(e){var t=e.components,n=Object(r.a)(e,["components"]);return Object(i.b)("wrapper",Object(o.a)({},u,n,{components:t,mdxType:"MDXLayout"}),Object(i.b)("h2",{id:"deploying-orca"},"Deploying ORCA"),Object(i.b)("p",null,"The following sections provide information on how to\ndeploy ORCA with or along-side Cumulus."),Object(i.b)("h3",{id:"setup-deployment-environment"},"Setup Deployment Environment"),Object(i.b)("p",null,"In order to deploy ORCA into an NGAP environment with\nCumulus, a deployment environment needs be created."),Object(i.b)("p",null,"Visit ",Object(i.b)("a",Object(o.a)({parentName:"p"},{href:"/cumulus-orca/docs/developer/deployment-guide/deployment-environment"}),"Creating a Deployment Environment"),"\nto view the instructions for setting up your ORCA deployment environment."),Object(i.b)("h3",{id:"orca-archive-bucket"},"ORCA Archive Bucket"),Object(i.b)("p",null,"ORCA maintains a cloud ready backup of science and\nancillary data in an S3-IA bucket and utilizes AWS\nbucket transition policies to store the data in S3\nGlacier for the long term. The ORCA archive bucket can\nlive in any NGAP Organizational Unit (OU)."),Object(i.b)("p",null,"Visit ",Object(i.b)("a",Object(o.a)({parentName:"p"},{href:"/cumulus-orca/docs/developer/deployment-guide/deployment-s3-bucket"}),"Creating the Glacier Bucket"),"\nto view the instructions for setting up a Glacier\nbucket."),Object(i.b)("div",{className:"admonition admonition-important alert alert--info"},Object(i.b)("div",Object(o.a)({parentName:"div"},{className:"admonition-heading"}),Object(i.b)("h5",{parentName:"div"},Object(i.b)("span",Object(o.a)({parentName:"h5"},{className:"admonition-icon"}),Object(i.b)("svg",Object(o.a)({parentName:"span"},{xmlns:"http://www.w3.org/2000/svg",width:"14",height:"16",viewBox:"0 0 14 16"}),Object(i.b)("path",Object(o.a)({parentName:"svg"},{fillRule:"evenodd",d:"M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"})))),"important")),Object(i.b)("div",Object(o.a)({parentName:"div"},{className:"admonition-content"}),Object(i.b)("p",{parentName:"div"},"Prior to deploying ORCA with Cumulus, the ORCA archive bucket must be\ncreated."))),Object(i.b)("h3",{id:"deploy-orca-with-cumulus"},"Deploy ORCA with Cumulus"),Object(i.b)("p",null,"After the ORCA archive bucket has been created, ORCA is ready to be\ndeployed. Visit ",Object(i.b)("a",Object(o.a)({parentName:"p"},{href:"/cumulus-orca/docs/developer/deployment-guide/deployment-with-cumulus"}),"ORCA deployment documentation"),"\nfor instructions to deploy ORCA with Cumulus."),Object(i.b)("h2",{id:"configuring-orca"},"Configuring ORCA"),Object(i.b)("p",null,"Once ORCA is deployed, configure the collection in the Cumulus Dashboard for utilizing ORCA. See ",Object(i.b)("a",Object(o.a)({parentName:"p"},{href:"/cumulus-orca/docs/developer/deployment-guide/deployment-with-cumulus#collection-configuration"}),"ORCA Configuration"),"\nfor instructions."))}d.isMDXComponent=!0}}]);