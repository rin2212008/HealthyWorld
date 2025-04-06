import os
import re
import plistlib

def find_swift_files(directory):
    swift_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.swift'):
                swift_files.append(os.path.join(root, file))
    return swift_files

def update_project_file(project_path, swift_files):
    with open(project_path, 'r') as f:
        content = f.read()
    
    # Find the Sources build phase
    sources_phase = re.search(r'/\* Begin PBXSourcesBuildPhase section \*/(.*?)/\* End PBXSourcesBuildPhase section \*/', content, re.DOTALL)
    if not sources_phase:
        print("Could not find Sources build phase")
        return
    
    # Create new file references
    file_refs = []
    for swift_file in swift_files:
        file_name = os.path.basename(swift_file)
        file_ref = f'		3E7503B12DA2080F005958DE /* {file_name} */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = {file_name}; sourceTree = "<group>"; }};'
        file_refs.append(file_ref)
    
    # Create new build file references
    build_files = []
    for swift_file in swift_files:
        file_name = os.path.basename(swift_file)
        build_file = f'				3E7503B12DA2080F005958DE /* {file_name} in Sources */,'
        build_files.append(build_file)
    
    # Update the content
    new_content = content.replace(
        '/* Begin PBXFileReference section */',
        '/* Begin PBXFileReference section */\n' + '\n'.join(file_refs)
    )
    
    new_content = new_content.replace(
        '/* Begin PBXSourcesBuildPhase section */',
        '/* Begin PBXSourcesBuildPhase section */\n' + '\n'.join(build_files)
    )
    
    with open(project_path, 'w') as f:
        f.write(new_content)

def create_project_file():
    # Create the project directory if it doesn't exist
    project_dir = 'HealthyWorld2.xcodeproj'
    os.makedirs(project_dir, exist_ok=True)
    
    # Create the project file content
    project_content = '''// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 77;
	objects = {
/* Begin PBXBuildFile section */
		3E7503B12DA2080F005958DE /* HealthyWorld2App.swift in Sources */ = {isa = PBXBuildFile; fileRef = 3E7503B12DA2080F005958DE /* HealthyWorld2App.swift */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		3E7503B12DA2080F005958DE /* HealthyWorld2.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = HealthyWorld2.app; sourceTree = BUILT_PRODUCTS_DIR; };
		3E7503B12DA2080F005958DE /* HealthyWorld2App.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HealthyWorld2App.swift; sourceTree = "<group>"; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		3E7503AF2DA2080F005958DE /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		3E7503A92DA2080F005958DE = {
			isa = PBXGroup;
			children = (
				3E7503B12DA2080F005958DE /* HealthyWorld2 */,
				3E7503B32DA2080F005958DE /* Products */,
			);
			sourceTree = "<group>";
		};
		3E7503B32DA2080F005958DE /* Products */ = {
			isa = PBXGroup;
			children = (
				3E7503B12DA2080F005958DE /* HealthyWorld2.app */,
			);
			name = Products;
			sourceTree = "<group>";
		};
		3E7503B12DA2080F005958DE /* HealthyWorld2 */ = {
			isa = PBXGroup;
			children = (
				3E7503B12DA2080F005958DE /* HealthyWorld2App.swift */,
			);
			path = HealthyWorld2;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		3E7503B12DA2080F005958DE /* HealthyWorld2 */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 3E7503D32DA2081F005958DE /* Build configuration list for PBXNativeTarget "HealthyWorld2" */;
			buildPhases = (
				3E7503AE2DA2080F005958DE /* Sources */,
				3E7503AF2DA2080F005958DE /* Frameworks */,
				3E7503B02DA2080F005958DE /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = HealthyWorld2;
			productName = HealthyWorld2;
			productReference = 3E7503B12DA2080F005958DE /* HealthyWorld2.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		3E7503AA2DA2080F005958DE /* Project object */ = {
			isa = PBXProject;
			attributes = {
				BuildIndependentTargetsInParallel = 1;
				LastSwiftUpdateCheck = 1630;
				LastUpgradeCheck = 1630;
				TargetAttributes = {
					3E7503B12DA2080F005958DE = {
						CreatedOnToolsVersion = 16.3;
						LastSwiftMigration = 1630;
					};
				};
			};
			buildConfigurationList = 3E7503AD2DA2080F005958DE /* Build configuration list for PBXProject "HealthyWorld2" */;
			compatibilityVersion = "Xcode 16.0";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = 3E7503A92DA2080F005958DE;
			productRefGroup = 3E7503B32DA2080F005958DE /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				3E7503B12DA2080F005958DE /* HealthyWorld2 */,
			);
		};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		3E7503B02DA2080F005958DE /* Resources */ = {
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		3E7503AE2DA2080F005958DE /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				3E7503B12DA2080F005958DE /* HealthyWorld2App.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		3E7503D12DA2081F005958DE /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 17.0;
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				MTL_FAST_MATH = YES;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = iphoneos;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
			};
			name = Debug;
		};
		3E7503D22DA2081F005958DE /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				IPHONEOS_DEPLOYMENT_TARGET = 17.0;
				MTL_ENABLE_DEBUG_INFO = NO;
				MTL_FAST_MATH = YES;
				SDKROOT = iphoneos;
				SWIFT_COMPILATION_MODE = wholemodule;
				SWIFT_OPTIMIZATION_LEVEL = "-O";
				VALIDATE_PRODUCT = YES;
			};
			name = Release;
		};
		3E7503D42DA2081F005958DE /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_ASSET_PATHS = "\"HealthyWorld2/Preview Content\"";
				DEVELOPMENT_TEAM = "";
				ENABLE_PREVIEWS = YES;
				GENERATE_INFOPLIST_FILE = YES;
				INFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;
				INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;
				INFOPLIST_KEY_UILaunchScreen_Generation = YES;
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPhone = "UIInterfaceOrientationPortrait UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.example.HealthyWorld2;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Debug;
		};
		3E7503D52DA2081F005958DE /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_ASSET_PATHS = "\"HealthyWorld2/Preview Content\"";
				DEVELOPMENT_TEAM = "";
				ENABLE_PREVIEWS = YES;
				GENERATE_INFOPLIST_FILE = YES;
				INFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;
				INFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;
				INFOPLIST_KEY_UILaunchScreen_Generation = YES;
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				INFOPLIST_KEY_UISupportedInterfaceOrientations_iPhone = "UIInterfaceOrientationPortrait UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.example.HealthyWorld2;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		3E7503AD2DA2080F005958DE /* Build configuration list for PBXProject "HealthyWorld2" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				3E7503D12DA2081F005958DE /* Debug */,
				3E7503D22DA2081F005958DE /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		3E7503D32DA2081F005958DE /* Build configuration list for PBXNativeTarget "HealthyWorld2" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				3E7503D42DA2081F005958DE /* Debug */,
				3E7503D52DA2081F005958DE /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */
	};
	rootObject = 3E7503AA2DA2080F005958DE /* Project object */;
}'''
    
    # Write the project file
    project_path = os.path.join(project_dir, 'project.pbxproj')
    with open(project_path, 'w') as f:
        f.write(project_content)
    
    print(f"Project file created at {project_path}")

def main():
    project_dir = 'HealthyWorld2.xcodeproj'
    project_file = os.path.join(project_dir, 'project.pbxproj')
    swift_files = find_swift_files('HealthyWorld2')
    
    update_project_file(project_file, swift_files)
    print("Project file updated successfully")

if __name__ == '__main__':
    create_project_file() 