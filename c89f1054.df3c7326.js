(window.webpackJsonp=window.webpackJsonp||[]).push([[31],{108:function(e,t,n){"use strict";n.d(t,"a",(function(){return p})),n.d(t,"b",(function(){return m}));var r=n(0),o=n.n(r);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function l(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function c(e,t){if(null==e)return{};var n,r,o=function(e,t){if(null==e)return{};var n,r,o={},a=Object.keys(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)n=a[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var u=o.a.createContext({}),s=function(e){var t=o.a.useContext(u),n=t;return e&&(n="function"==typeof e?e(t):l(l({},t),e)),n},p=function(e){var t=s(e.components);return o.a.createElement(u.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return o.a.createElement(o.a.Fragment,{},t)}},b=o.a.forwardRef((function(e,t){var n=e.components,r=e.mdxType,a=e.originalType,i=e.parentName,u=c(e,["components","mdxType","originalType","parentName"]),p=s(n),b=r,m=p["".concat(i,".").concat(b)]||p[b]||d[b]||a;return n?o.a.createElement(m,l(l({ref:t},u),{},{components:n})):o.a.createElement(m,l({ref:t},u))}));function m(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var a=n.length,i=new Array(a);i[0]=b;var l={};for(var c in t)hasOwnProperty.call(t,c)&&(l[c]=t[c]);l.originalType=e,l.mdxType="string"==typeof e?e:r,i[1]=l;for(var u=2;u<a;u++)i[u]=n[u];return o.a.createElement.apply(null,i)}return o.a.createElement.apply(null,n)}b.displayName="MDXCreateElement"},98:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return i})),n.d(t,"metadata",(function(){return l})),n.d(t,"rightToc",(function(){return c})),n.d(t,"default",(function(){return s}));var r=n(3),o=n(7),a=(n(0),n(108)),i={id:"contrib-documentation-env",title:"Development Environment",desc:"Provides basic information on setting up an ORCA documentation development environment."},l={unversionedId:"developer/development-guide/documentation/contrib-documentation-env",id:"developer/development-guide/documentation/contrib-documentation-env",isDocsHomePage:!1,title:"Development Environment",description:"Editing and updating the website only requires a text editor and git but, in",source:"@site/docs/developer/development-guide/documentation/documentation-dev-env.md",slug:"/developer/development-guide/documentation/contrib-documentation-env",permalink:"/cumulus-orca/docs/developer/development-guide/documentation/contrib-documentation-env",editUrl:"https://github.com/nasa/cumulus-orca/edit/develop/website/docs/developer/development-guide/documentation/documentation-dev-env.md",version:"current",sidebar:"dev_guide",previous:{title:"Documentation Introduction",permalink:"/cumulus-orca/docs/developer/development-guide/documentation/contrib-documentation-intro"},next:{title:"Adding New Content",permalink:"/cumulus-orca/docs/developer/development-guide/documentation/contrib-documentation-add"}},c=[{value:"Creating the Development Environment",id:"creating-the-development-environment",children:[]},{value:"Installing the Test Harness",id:"installing-the-test-harness",children:[]},{value:"Running the Development Server",id:"running-the-development-server",children:[]},{value:"Building the ORCA Website Locally",id:"building-the-orca-website-locally",children:[]}],u={rightToc:c};function s(e){var t=e.components,n=Object(o.a)(e,["components"]);return Object(a.b)("wrapper",Object(r.a)({},u,n,{components:t,mdxType:"MDXLayout"}),Object(a.b)("p",null,"Editing and updating the website only requires a text editor and git but, in\norder to verify links and the overall website build, a local development environment\nshould be created. This pages discusses the setup, running, building, and testing\nof the Docusarus website for the ORCA GitHub pages."),Object(a.b)("h2",{id:"creating-the-development-environment"},"Creating the Development Environment"),Object(a.b)("p",null,"Setting up the development environment consists of three primary tasks,"),Object(a.b)("ul",null,Object(a.b)("li",{parentName:"ul"},"Cloning the cumulus-orca GitHub repository"),Object(a.b)("li",{parentName:"ul"},"Installing the proper Node.js and npm versions"),Object(a.b)("li",{parentName:"ul"},"Installing the proper node packages for the cumulus-orca documentation.")),Object(a.b)("p",null,"The installation steps below goes into further details."),Object(a.b)("ol",null,Object(a.b)("li",{parentName:"ol"},Object(a.b)("p",{parentName:"li"},"Install the latest ",Object(a.b)("a",Object(r.a)({parentName:"p"},{href:"https://github.com/nvm-sh/nvm"}),"Node Version Manager (nvm)")," application to manage Node.js and npm versions."),Object(a.b)("pre",{parentName:"li"},Object(a.b)("code",Object(r.a)({parentName:"pre"},{className:"language-sh"}),"curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash\n"))),Object(a.b)("li",{parentName:"ol"},Object(a.b)("p",{parentName:"li"},"Install the proper Node.js and npm versions to your machine. Currently Node v12.15.0 should be used."),Object(a.b)("pre",{parentName:"li"},Object(a.b)("code",Object(r.a)({parentName:"pre"},{className:"language-sh"}),"nvm install 12.15.0\nnvm use 12.15.0\nnpm install npm@latest -g\n"))),Object(a.b)("li",{parentName:"ol"},Object(a.b)("p",{parentName:"li"},"Clone the cumulus-orca repository to your local machine."),Object(a.b)("pre",{parentName:"li"},Object(a.b)("code",Object(r.a)({parentName:"pre"},{className:"language-sh"}),"git clone https://github.com/nasa/cumulus-orca.git\n"))),Object(a.b)("li",{parentName:"ol"},Object(a.b)("p",{parentName:"li"},"Move to the ",Object(a.b)("inlineCode",{parentName:"p"},"website")," directory under the cumulus-orca local git repository."),Object(a.b)("pre",{parentName:"li"},Object(a.b)("code",Object(r.a)({parentName:"pre"},{className:"language-sh"}),"cd cumulus-orca/website\n"))),Object(a.b)("li",{parentName:"ol"},Object(a.b)("p",{parentName:"li"},"Install the additional node packages needed to create and validate the webpages."),Object(a.b)("pre",{parentName:"li"},Object(a.b)("code",Object(r.a)({parentName:"pre"},{className:"language-sh"}),"npm install\n")))),Object(a.b)("h2",{id:"installing-the-test-harness"},"Installing the Test Harness"),Object(a.b)("p",null,"TBD - Automated testing that includes link checking is currently being looked into."),Object(a.b)("h2",{id:"running-the-development-server"},"Running the Development Server"),Object(a.b)("p",null,"To run the development web server and verify builds, contents, and styles perform\nthe following commands. More information on running a Docusaurus website can be\nfound in the ",Object(a.b)("a",Object(r.a)({parentName:"p"},{href:"https://v2.docusaurus.io/docs/installation#running-the-development-server"}),"Docusaurus documentation"),"."),Object(a.b)("pre",null,Object(a.b)("code",Object(r.a)({parentName:"pre"},{className:"language-sh"}),"## From the repository base move to the website directory.\ncd website\n\n## Start the server on port 8080 with verbose output for debuging\nnpm run start --verbose -- --port 8080\n")),Object(a.b)("p",null,"A new webpage should display in your default browser at ",Object(a.b)("a",Object(r.a)({parentName:"p"},{href:"http://localhost:8080"}),"http://localhost:8080"),"."),Object(a.b)("h2",{id:"building-the-orca-website-locally"},"Building the ORCA Website Locally"),Object(a.b)("p",null,"To build the cumulus-orca static website for GitHub pages locally run the\ncommands seen below. More information on building a Docusaurus website can be\nfound in the ",Object(a.b)("a",Object(r.a)({parentName:"p"},{href:"https://v2.docusaurus.io/docs/installation#build"}),"Docusaurus documentation"),"."),Object(a.b)("pre",null,Object(a.b)("code",Object(r.a)({parentName:"pre"},{className:"language-sh"}),"## From the repository base move to the website directory.\ncd website\n\n## Build the site\nnpm run build\n")),Object(a.b)("p",null,"The resulting site can be found in the ",Object(a.b)("inlineCode",{parentName:"p"},"build")," directory."))}s.isMDXComponent=!0}}]);