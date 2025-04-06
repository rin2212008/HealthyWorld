#!/usr/bin/env python3

import os
import re
import uuid

def generate_uuid():
    return str(uuid.uuid4()).upper().replace('-', '')[:24]

def fix_build_phases(project_path):
    # Read the project file
    with open(project_path, 'r') as f:
        content = f.read()

    # Find the main target section
    main_target_section = re.search(r'/\* Begin PBXNativeTarget section \*/(.*?)/\* End PBXNativeTarget section \*/', content, re.DOTALL)
    if not main_target_section:
        print("Could not find main target section")
        return

    # Get all Swift files
    swift_files = []
    for root, _, files in os.walk('HealthyWorld2'):
        for file in files:
            if file.endswith('.swift'):
                swift_files.append(os.path.join(root, file))

    # Generate new build phase content
    sources_build_phase = '''/* Begin PBXSourcesBuildPhase section */
        3E7503AE2DA2080F005958DE /* Sources */ = {
            isa = PBXSourcesBuildPhase;
            buildActionMask = 2147483647;
            files = (
                ''' + ',\n                '.join([f'{generate_uuid()} /* {os.path.basename(f)} in Sources */ = {{isa = PBXBuildFile; fileRef = {generate_uuid()} /* {os.path.basename(f)} */; }};' for f in swift_files]) + '''
            );
            runOnlyForDeploymentPostprocessing = 0;
        };
/* End PBXSourcesBuildPhase section */'''

    frameworks_build_phase = '''/* Begin PBXFrameworksBuildPhase section */
        3E7503AF2DA2080F005958DE /* Frameworks */ = {
            isa = PBXFrameworksBuildPhase;
            buildActionMask = 2147483647;
            files = (
                ''' + f'{generate_uuid()} /* SwiftUI.framework in Frameworks */ = {{isa = PBXBuildFile; fileRef = {generate_uuid()} /* SwiftUI.framework */; }},\n                ' + f'{generate_uuid()} /* Foundation.framework in Frameworks */ = {{isa = PBXBuildFile; fileRef = {generate_uuid()} /* Foundation.framework */; }},' + '''
            );
            runOnlyForDeploymentPostprocessing = 0;
        };
/* End PBXFrameworksBuildPhase section */'''

    resources_build_phase = '''/* Begin PBXResourcesBuildPhase section */
        3E7503B02DA2080F005958DE /* Resources */ = {
            isa = PBXResourcesBuildPhase;
            buildActionMask = 2147483647;
            files = (
                ''' + f'{generate_uuid()} /* Assets.xcassets in Resources */ = {{isa = PBXBuildFile; fileRef = {generate_uuid()} /* Assets.xcassets */; }},' + '''
            );
            runOnlyForDeploymentPostprocessing = 0;
        };
/* End PBXResourcesBuildPhase section */'''

    # Replace the old build phases with the new ones
    content = re.sub(r'/\* Begin PBXSourcesBuildPhase section \*/(.*?)/\* End PBXSourcesBuildPhase section \*/', 
                    sources_build_phase, content, flags=re.DOTALL)
    content = re.sub(r'/\* Begin PBXFrameworksBuildPhase section \*/(.*?)/\* End PBXFrameworksBuildPhase section \*/', 
                    frameworks_build_phase, content, flags=re.DOTALL)
    content = re.sub(r'/\* Begin PBXResourcesBuildPhase section \*/(.*?)/\* End PBXResourcesBuildPhase section \*/', 
                    resources_build_phase, content, flags=re.DOTALL)

    # Write the updated content back to the file
    with open(project_path, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    project_path = 'HealthyWorld2.xcodeproj/project.pbxproj'
    fix_build_phases(project_path)
    print("Build phases have been fixed. Please open the project in Xcode to verify the changes.") 