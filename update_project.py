import os
import re

def update_project_file(project_path):
    with open(project_path, 'r') as f:
        content = f.read()
    
    # Add scheme settings if they don't exist
    if 'LastSwiftUpdateCheck' not in content:
        new_content = content.replace(
            '/* Begin PBXProject section */',
            '''/* Begin PBXProject section */
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
		};'''
        )
    else:
        new_content = content
    
    with open(project_path, 'w') as f:
        f.write(new_content)
    
    print("Project file updated with scheme settings")

def main():
    project_dir = 'HealthyWorld2.xcodeproj'
    project_file = os.path.join(project_dir, 'project.pbxproj')
    update_project_file(project_file)

if __name__ == '__main__':
    main() 