import os
import plistlib
from datetime import datetime

def create_scheme():
    # Create the schemes directory if it doesn't exist
    schemes_dir = 'HealthyWorld2.xcodeproj/xcshareddata/xcschemes'
    os.makedirs(schemes_dir, exist_ok=True)
    
    # Create the scheme file content
    scheme_content = {
        'ArchiveAction': {
            'buildConfiguration': 'Release',
            'revealArchiveInOrganizer': True,
            'customArchiveName': 'HealthyWorld2'
        },
        'BuildAction': {
            'buildImplicitDependencies': True,
            'parallelizeBuildables': True,
            'buildActionEntries': [
                {
                    'buildForAnalyzing': True,
                    'buildForArchiving': True,
                    'buildForProfiling': True,
                    'buildForRunning': True,
                    'buildForTesting': True,
                    'buildableReference': {
                        'BuildableIdentifier': 'primary',
                        'BlueprintIdentifier': '3E7503B12DA2080F005958DE',
                        'BuildableName': 'HealthyWorld2.app',
                        'BlueprintName': 'HealthyWorld2',
                        'ReferencedContainer': 'container:HealthyWorld2.xcodeproj'
                    }
                }
            ]
        },
        'LaunchAction': {
            'buildConfiguration': 'Debug',
            'selectedDebuggerIdentifier': 'Xcode.DebuggerFoundation.Debugger.LLDB',
            'selectedLauncherIdentifier': 'Xcode.DebuggerFoundation.Launcher.LLDB',
            'launchStyle': '0',
            'useCustomWorkingDirectory': False,
            'ignoresPersistentStateOnLaunch': False,
            'debugDocumentVersioning': True,
            'debugServiceExtension': 'internal',
            'allowLocationSimulation': True,
            'buildableProductRunnable': {
                'BuildableIdentifier': 'primary',
                'BlueprintIdentifier': '3E7503B12DA2080F005958DE',
                'BuildableName': 'HealthyWorld2.app',
                'BlueprintName': 'HealthyWorld2',
                'ReferencedContainer': 'container:HealthyWorld2.xcodeproj'
            }
        },
        'ProfileAction': {
            'buildConfiguration': 'Release',
            'shouldUseLaunchSchemeArgsEnv': True,
            'savedToolIdentifier': '',
            'useCustomWorkingDirectory': False,
            'debugDocumentVersioning': True,
            'buildableProductRunnable': {
                'BuildableIdentifier': 'primary',
                'BlueprintIdentifier': '3E7503B12DA2080F005958DE',
                'BuildableName': 'HealthyWorld2.app',
                'BlueprintName': 'HealthyWorld2',
                'ReferencedContainer': 'container:HealthyWorld2.xcodeproj'
            }
        },
        'TestAction': {
            'buildConfiguration': 'Debug',
            'selectedDebuggerIdentifier': 'Xcode.DebuggerFoundation.Debugger.LLDB',
            'selectedLauncherIdentifier': 'Xcode.DebuggerFoundation.Launcher.LLDB',
            'shouldUseLaunchSchemeArgsEnv': True,
            'codeCoverageEnabled': False,
            'onlyGenerateCoverageForSpecifiedTargets': False,
            'useCustomWorkingDirectory': False,
            'buildableProductRunnable': {
                'BuildableIdentifier': 'primary',
                'BlueprintIdentifier': '3E7503B12DA2080F005958DE',
                'BuildableName': 'HealthyWorld2.app',
                'BlueprintName': 'HealthyWorld2',
                'ReferencedContainer': 'container:HealthyWorld2.xcodeproj'
            }
        },
        'AnalyzeAction': {
            'buildConfiguration': 'Debug'
        },
        'SchemeName': 'HealthyWorld2',
        'WasCreatedForAppExtension': False,
        'LastUpgradeVersion': '1630'
    }
    
    # Write the scheme file
    scheme_path = os.path.join(schemes_dir, 'HealthyWorld2.xcscheme')
    with open(scheme_path, 'wb') as f:
        plistlib.dump(scheme_content, f)
    
    print(f"Scheme file created at {scheme_path}")

if __name__ == '__main__':
    create_scheme() 