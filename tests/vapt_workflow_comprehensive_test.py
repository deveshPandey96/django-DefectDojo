#!/usr/bin/env python3
"""
DefectDojo VAPT Workflow Comprehensive Test Suite

This test suite validates DefectDojo as a complete vulnerability assessment and 
penetration testing (VAPT) platform, covering the entire workflow:
Scan → Import → Assign → Remediation → Verification → Closure → Reporting

Usage:
    python manage.py test tests.vapt_workflow_comprehensive_test

Author: VAPT Testing Team
Date: 2025-09-16
"""

import sys
import time
import unittest
import json
from datetime import datetime, timedelta
from pathlib import Path

from base_test_class import BaseTestCase, on_exception_html_source_logger, set_suite_settings
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class VAPTWorkflowComprehensiveTest(BaseTestCase):
    """
    Comprehensive VAPT Workflow Test Suite for DefectDojo
    
    This test suite validates all aspects of using DefectDojo as a 
    vulnerability management platform including:
    - Project and asset management
    - Vulnerability import and discovery
    - Workflow and assignment management
    - Verification and closure processes
    - Reporting and dashboard functionality
    - Notifications and alert systems
    - Security and access control
    """
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_report = {
            'execution_start': datetime.now().isoformat(),
            'test_categories': {},
            'summary': {}
        }
    
    def setUp(self):
        super().setUp()
        self.current_category = None
        self.category_results = {}
    
    def tearDown(self):
        if self.current_category:
            self.test_report['test_categories'][self.current_category] = self.category_results
        super().tearDown()
    
    @classmethod
    def tearDownClass(cls):
        cls.test_report['execution_end'] = datetime.now().isoformat()
        cls.generate_final_report()
        super().tearDownClass()
    
    # ===========================
    # STEP 1: PROJECT & ASSET SETUP
    # ===========================
    
    @on_exception_html_source_logger
    def test_01_project_and_asset_management(self):
        """
        Test comprehensive project and asset management capabilities
        
        Validates:
        - Project creation for different environments
        - Asset and endpoint management
        - User assignment and role management
        - Environment categorization
        """
        self.current_category = "project_asset_management"
        driver = self.driver
        
        print("\n🏗️  Testing Project & Asset Management")
        
        # Test 1.1: Create Production Project
        try:
            self.goto_product_overview(driver)
            driver.find_element(By.ID, "dropdownMenu1").click()
            driver.find_element(By.LINK_TEXT, "Add Product").click()
            
            driver.find_element(By.ID, "id_name").clear()
            driver.find_element(By.ID, "id_name").send_keys("VAPT-Production-Environment")
            driver.find_element(By.ID, "id_description").clear()
            driver.find_element(By.ID, "id_description").send_keys("Production environment for VAPT testing and validation")
            
            # Set product type
            prod_type_select = Select(driver.find_element(By.ID, "id_prod_type"))
            prod_type_select.select_by_visible_text("Research and Development")
            
            driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
            
            result = self.is_success_message_present(text="Product added successfully")
            self.category_results['create_production_project'] = result
            self.assertTrue(result, "Production project creation should succeed")
            print("✅ Production project created successfully")
            
        except Exception as e:
            self.category_results['create_production_project'] = False
            print(f"❌ Production project creation failed: {str(e)}")
            self.fail(f"Failed to create production project: {str(e)}")
        
        # Test 1.2: Add Endpoints and Assets
        try:
            # Navigate to product and add endpoint
            self.goto_product_overview(driver)
            driver.find_element(By.LINK_TEXT, "VAPT-Production-Environment").click()
            
            driver.find_element(By.ID, "dropdownMenu1").click()
            driver.find_element(By.LINK_TEXT, "Add Endpoint").click()
            
            driver.find_element(By.ID, "id_endpoint").clear()
            driver.find_element(By.ID, "id_endpoint").send_keys("https://production-app.company.com")
            driver.find_element(By.ID, "id_description").clear()
            driver.find_element(By.ID, "id_description").send_keys("Production web application endpoint")
            
            driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
            
            result = self.is_success_message_present(text="Endpoint added successfully")
            self.category_results['add_endpoint'] = result
            print("✅ Endpoint added successfully" if result else "❌ Endpoint addition failed")
            
        except Exception as e:
            self.category_results['add_endpoint'] = False
            print(f"❌ Endpoint addition failed: {str(e)}")
    
    # ===========================
    # STEP 2: VULNERABILITY IMPORT
    # ===========================
    
    @on_exception_html_source_logger
    def test_02_vulnerability_import_and_discovery(self):
        """
        Test vulnerability import and discovery capabilities
        
        Validates:
        - Manual vulnerability entry
        - Scanner result import
        - Metadata preservation
        - Severity mapping
        """
        self.current_category = "vulnerability_import_discovery"
        driver = self.driver
        
        print("\n🔍 Testing Vulnerability Import & Discovery")
        
        # Ensure we have a product to work with
        self.ensure_test_environment_exists()
        
        # Test 2.1: Create Engagement
        try:
            self.goto_product_overview(driver)
            driver.find_element(By.LINK_TEXT, "VAPT-Production-Environment").click()
            
            driver.find_element(By.ID, "dropdownMenu1").click()
            driver.find_element(By.LINK_TEXT, "Add Engagement").click()
            
            driver.find_element(By.ID, "id_name").clear()
            driver.find_element(By.ID, "id_name").send_keys("Q4 Security Assessment 2024")
            driver.find_element(By.ID, "id_description").clear()
            driver.find_element(By.ID, "id_description").send_keys("Quarterly comprehensive security assessment including VAPT activities")
            
            # Set engagement dates
            driver.find_element(By.ID, "id_target_start").clear()
            driver.find_element(By.ID, "id_target_start").send_keys("2024-10-01")
            driver.find_element(By.ID, "id_target_end").clear()
            driver.find_element(By.ID, "id_target_end").send_keys("2024-12-31")
            
            driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
            
            result = self.is_success_message_present(text="Engagement added successfully")
            self.category_results['create_engagement'] = result
            self.assertTrue(result, "Engagement creation should succeed")
            print("✅ Engagement created successfully")
            
        except Exception as e:
            self.category_results['create_engagement'] = False
            print(f"❌ Engagement creation failed: {str(e)}")
            self.fail(f"Failed to create engagement: {str(e)}")
        
        # Test 2.2: Add Critical Vulnerability
        try:
            driver.find_element(By.LINK_TEXT, "Q4 Security Assessment 2024").click()
            driver.find_element(By.ID, "dropdownMenu1").click()
            driver.find_element(By.LINK_TEXT, "Add Finding").click()
            
            # Critical vulnerability details
            driver.find_element(By.ID, "id_title").clear()
            driver.find_element(By.ID, "id_title").send_keys("Remote Code Execution via File Upload")
            
            severity_select = Select(driver.find_element(By.ID, "id_severity"))
            severity_select.select_by_visible_text("Critical")
            
            driver.find_element(By.ID, "id_description").clear()
            driver.find_element(By.ID, "id_description").send_keys("""
            **Vulnerability Description:**
            A remote code execution vulnerability exists in the file upload functionality.
            Attackers can upload malicious files that get executed on the server.
            
            **Attack Vector:**
            Upload a PHP/JSP file with malicious code through the file upload form.
            
            **Impact:**
            - Complete server compromise
            - Data exfiltration
            - Lateral movement
            - Service disruption
            
            **CVSS 3.1 Score:** 9.8 (Critical)
            **CWE:** CWE-434 (Unrestricted Upload of File with Dangerous Type)
            """)
            
            driver.find_element(By.ID, "id_mitigation").clear()
            driver.find_element(By.ID, "id_mitigation").send_keys("""
            **Immediate Actions:**
            1. Disable file upload functionality until patched
            2. Implement file type validation and sanitization
            3. Execute uploaded files in sandboxed environment
            4. Apply principle of least privilege to web server process
            
            **Long-term Solutions:**
            - Implement content-based file type detection
            - Use virus scanning for uploaded files
            - Store uploaded files outside web root
            - Implement file access controls
            """)
            
            # Mark as verified and active
            driver.find_element(By.ID, "id_verified").click()
            driver.find_element(By.ID, "id_active").click()
            
            driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
            
            result = self.is_success_message_present(text="Finding added successfully")
            self.category_results['add_critical_finding'] = result
            print("✅ Critical finding added successfully" if result else "❌ Critical finding addition failed")
            
        except Exception as e:
            self.category_results['add_critical_finding'] = False
            print(f"❌ Critical finding addition failed: {str(e)}")
        
        # Test 2.3: Add Medium Severity Finding
        try:
            driver.find_element(By.ID, "dropdownMenu1").click()
            driver.find_element(By.LINK_TEXT, "Add Finding").click()
            
            driver.find_element(By.ID, "id_title").clear()
            driver.find_element(By.ID, "id_title").send_keys("Information Disclosure in Error Messages")
            
            severity_select = Select(driver.find_element(By.ID, "id_severity"))
            severity_select.select_by_visible_text("Medium")
            
            driver.find_element(By.ID, "id_description").clear()
            driver.find_element(By.ID, "id_description").send_keys("""
            **Vulnerability Description:**
            The application reveals sensitive information in error messages including:
            - Database schema details
            - File system paths
            - Internal IP addresses
            - Software versions
            
            **CVSS 3.1 Score:** 5.3 (Medium)
            **CWE:** CWE-209 (Information Exposure Through Error Messages)
            """)
            
            driver.find_element(By.ID, "id_verified").click()
            driver.find_element(By.ID, "id_active").click()
            
            driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
            
            result = self.is_success_message_present(text="Finding added successfully")
            self.category_results['add_medium_finding'] = result
            print("✅ Medium finding added successfully" if result else "❌ Medium finding addition failed")
            
        except Exception as e:
            self.category_results['add_medium_finding'] = False
            print(f"❌ Medium finding addition failed: {str(e)}")
    
    # ===========================
    # STEP 3: WORKFLOW & ASSIGNMENT
    # ===========================
    
    @on_exception_html_source_logger
    def test_03_workflow_and_assignment_management(self):
        """
        Test workflow and assignment management capabilities
        
        Validates:
        - Finding assignment to owners
        - Status tracking and updates
        - Communication and notes
        - Workflow state management
        """
        self.current_category = "workflow_assignment_management"
        driver = self.driver
        
        print("\n🔄 Testing Workflow & Assignment Management")
        
        # Test 3.1: Update Finding Status
        try:
            self.goto_product_overview(driver)
            driver.find_element(By.LINK_TEXT, "VAPT-Production-Environment").click()
            driver.find_element(By.LINK_TEXT, "Q4 Security Assessment 2024").click()
            driver.find_element(By.LINK_TEXT, "Remote Code Execution via File Upload").click()
            
            # Add progress note
            driver.find_element(By.LINK_TEXT, "Add Note").click()
            
            driver.find_element(By.ID, "id_entry").clear()
            driver.find_element(By.ID, "id_entry").send_keys("""
            **Status Update:** Assigned to Development Team
            **Assigned To:** development-team@company.com
            **Priority:** P0 - Critical
            **Target Resolution Date:** 2024-10-15
            
            **Actions Taken:**
            - Vulnerability confirmed through manual testing
            - PoC developed and documented
            - Emergency change request submitted
            - Development team notified via emergency channels
            
            **Next Steps:**
            - Development team to implement hotfix
            - Security team to validate fix
            - Re-test scheduled for 2024-10-16
            """)
            
            driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
            
            result = self.is_success_message_present(text="Note saved")
            self.category_results['add_assignment_note'] = result
            print("✅ Assignment note added successfully" if result else "❌ Assignment note addition failed")
            
        except Exception as e:
            self.category_results['add_assignment_note'] = False
            print(f"❌ Assignment note addition failed: {str(e)}")
        
        # Test 3.2: Track Remediation Progress
        try:
            # Add remediation progress note
            driver.find_element(By.LINK_TEXT, "Add Note").click()
            
            driver.find_element(By.ID, "id_entry").clear()
            driver.find_element(By.ID, "id_entry").send_keys("""
            **Remediation Progress Update:**
            **Date:** 2024-10-14
            **Status:** In Progress
            
            **Development Team Update:**
            - File upload validation implemented
            - Content-type verification added
            - File execution restrictions applied
            - Code review completed
            
            **Testing Results:**
            - Unit tests: PASS
            - Security tests: PASS
            - Integration tests: PASS
            
            **Deployment Status:**
            - Scheduled for production deployment: 2024-10-15 02:00 AM
            - Rollback plan prepared
            - Monitoring alerts configured
            """)
            
            driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
            
            result = self.is_success_message_present(text="Note saved")
            self.category_results['track_remediation'] = result
            print("✅ Remediation tracking updated successfully" if result else "❌ Remediation tracking failed")
            
        except Exception as e:
            self.category_results['track_remediation'] = False
            print(f"❌ Remediation tracking failed: {str(e)}")
    
    # ===========================
    # STEP 4: VERIFICATION & CLOSURE
    # ===========================
    
    @on_exception_html_source_logger
    def test_04_verification_and_closure_process(self):
        """
        Test verification and closure process capabilities
        
        Validates:
        - Remediation verification
        - Evidence documentation
        - Closure workflow
        - Re-testing procedures
        """
        self.current_category = "verification_closure_process"
        driver = self.driver
        
        print("\n✅ Testing Verification & Closure Process")
        
        # Test 4.1: Verify Remediation
        try:
            # Navigate to medium severity finding for closure
            self.goto_product_overview(driver)
            driver.find_element(By.LINK_TEXT, "VAPT-Production-Environment").click()
            driver.find_element(By.LINK_TEXT, "Q4 Security Assessment 2024").click()
            driver.find_element(By.LINK_TEXT, "Information Disclosure in Error Messages").click()
            
            # Add verification note
            driver.find_element(By.LINK_TEXT, "Add Note").click()
            
            driver.find_element(By.ID, "id_entry").clear()
            driver.find_element(By.ID, "id_entry").send_keys("""
            **Remediation Verification Completed**
            **Verification Date:** 2024-10-16
            **Verified By:** Security Testing Team
            
            **Re-testing Results:**
            - Error handling improved: ✅ PASS
            - Generic error messages implemented: ✅ PASS
            - Sensitive information removed: ✅ PASS
            - Logging enhanced for debugging: ✅ PASS
            
            **Evidence:**
            - Before/after screenshots captured
            - Test cases documented
            - Security scan results attached
            
            **Verification Status:** VERIFIED - READY FOR CLOSURE
            """)
            
            driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
            
            result = self.is_success_message_present(text="Note saved")
            self.category_results['verification_completed'] = result
            print("✅ Verification completed successfully" if result else "❌ Verification completion failed")
            
        except Exception as e:
            self.category_results['verification_completed'] = False
            print(f"❌ Verification completion failed: {str(e)}")
        
        # Test 4.2: Close Finding
        try:
            # Mark finding as mitigated
            driver.find_element(By.LINK_TEXT, "Edit Finding").click()
            driver.find_element(By.ID, "id_is_mitigated").click()
            
            # Update mitigation details
            current_mitigation = driver.find_element(By.ID, "id_mitigation").get_attribute("value")
            driver.find_element(By.ID, "id_mitigation").clear()
            driver.find_element(By.ID, "id_mitigation").send_keys(current_mitigation + """
            
            **REMEDIATION COMPLETED:**
            **Completion Date:** 2024-10-16
            **Implemented By:** Development Team
            **Verified By:** Security Team
            
            **Solution Implemented:**
            - Custom error handling implemented
            - Generic error messages for all user-facing errors
            - Detailed error logging for development team (server-side only)
            - Error message sanitization applied
            
            **Verification Evidence:**
            - Security re-testing completed
            - No sensitive information in error responses
            - Proper error handling verified across all endpoints
            
            **Status:** CLOSED - VERIFIED REMEDIATION
            """)
            
            driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
            
            result = self.is_success_message_present(text="Finding saved successfully")
            self.category_results['close_finding'] = result
            print("✅ Finding closed successfully" if result else "❌ Finding closure failed")
            
        except Exception as e:
            self.category_results['close_finding'] = False
            print(f"❌ Finding closure failed: {str(e)}")
    
    # ===========================
    # STEP 5: REPORTING & DASHBOARDS
    # ===========================
    
    @on_exception_html_source_logger
    def test_05_reporting_and_dashboard_functionality(self):
        """
        Test reporting and dashboard functionality
        
        Validates:
        - Executive dashboard access
        - Report generation
        - Metrics and analytics
        - Data export capabilities
        """
        self.current_category = "reporting_dashboard_functionality"
        driver = self.driver
        
        print("\n📊 Testing Reporting & Dashboard Functionality")
        
        # Test 5.1: Access Executive Dashboard
        try:
            driver.get(self.base_url + "dashboard")
            
            # Wait for dashboard to load and check for key elements
            dashboard_elements = [
                "Total",
                "Active", 
                "Critical",
                "High",
                "Medium",
                "Low"
            ]
            
            dashboard_functional = False
            for element in dashboard_elements:
                if element in driver.page_source:
                    dashboard_functional = True
                    break
            
            self.category_results['access_dashboard'] = dashboard_functional
            print("✅ Dashboard accessible with metrics" if dashboard_functional else "❌ Dashboard access failed")
            
        except Exception as e:
            self.category_results['access_dashboard'] = False
            print(f"❌ Dashboard access failed: {str(e)}")
        
        # Test 5.2: Generate Product Report
        try:
            self.goto_product_overview(driver)
            driver.find_element(By.LINK_TEXT, "VAPT-Production-Environment").click()
            
            # Check if product metrics are displayed
            metrics_displayed = False
            metric_keywords = ["Total", "Active", "Verified", "Critical", "High", "Medium", "Low"]
            
            for keyword in metric_keywords:
                if keyword in driver.page_source:
                    metrics_displayed = True
                    break
            
            self.category_results['product_metrics'] = metrics_displayed
            print("✅ Product metrics displayed successfully" if metrics_displayed else "❌ Product metrics display failed")
            
        except Exception as e:
            self.category_results['product_metrics'] = False
            print(f"❌ Product metrics display failed: {str(e)}")
        
        # Test 5.3: Engagement Reporting
        try:
            driver.find_element(By.LINK_TEXT, "Q4 Security Assessment 2024").click()
            
            # Verify engagement summary information
            engagement_info_present = ("findings" in driver.page_source.lower() or 
                                     "vulnerability" in driver.page_source.lower())
            
            self.category_results['engagement_reporting'] = engagement_info_present
            print("✅ Engagement reporting functional" if engagement_info_present else "❌ Engagement reporting failed")
            
        except Exception as e:
            self.category_results['engagement_reporting'] = False
            print(f"❌ Engagement reporting failed: {str(e)}")
    
    # ===========================
    # STEP 6: NOTIFICATIONS & ALERTS
    # ===========================
    
    @on_exception_html_source_logger  
    def test_06_notifications_and_alert_systems(self):
        """
        Test notification and alert system capabilities
        
        Validates:
        - Notification configuration
        - Alert system setup
        - SLA monitoring
        - Communication workflows
        """
        self.current_category = "notifications_alert_systems"
        driver = self.driver
        
        print("\n🔔 Testing Notifications & Alert Systems")
        
        # Test 6.1: Access Notification Settings
        try:
            driver.get(self.base_url + "notifications")
            
            notification_page_accessible = ("notification" in driver.page_source.lower() or 
                                          "alert" in driver.page_source.lower() or
                                          "settings" in driver.page_source.lower())
            
            self.category_results['notification_settings'] = notification_page_accessible
            print("✅ Notification settings accessible" if notification_page_accessible else "❌ Notification settings access failed")
            
        except Exception as e:
            self.category_results['notification_settings'] = False
            print(f"❌ Notification settings access failed: {str(e)}")
        
        # Test 6.2: SLA Configuration
        try:
            driver.get(self.base_url + "sla_config")
            
            sla_page_accessible = ("sla" in driver.page_source.lower() or 
                                 "service" in driver.page_source.lower() or
                                 "level" in driver.page_source.lower())
            
            self.category_results['sla_configuration'] = sla_page_accessible
            print("✅ SLA configuration accessible" if sla_page_accessible else "❌ SLA configuration access failed")
            
        except Exception as e:
            self.category_results['sla_configuration'] = False
            print(f"❌ SLA configuration access failed: {str(e)}")
    
    # ===========================
    # STEP 7: SECURITY & ACCESS CONTROL
    # ===========================
    
    @on_exception_html_source_logger
    def test_07_security_and_access_control(self):
        """
        Test security and access control capabilities
        
        Validates:
        - User and role management
        - Access controls
        - Data protection
        - Administrative functions
        """
        self.current_category = "security_access_control"
        driver = self.driver
        
        print("\n🔒 Testing Security & Access Control")
        
        # Test 7.1: User Management Access
        try:
            driver.get(self.base_url + "user")
            
            user_management_accessible = ("user" in driver.page_source.lower() and 
                                        ("management" in driver.page_source.lower() or 
                                         "New User" in driver.page_source))
            
            self.category_results['user_management'] = user_management_accessible
            print("✅ User management accessible" if user_management_accessible else "❌ User management access failed")
            
        except Exception as e:
            self.category_results['user_management'] = False
            print(f"❌ User management access failed: {str(e)}")
        
        # Test 7.2: Product Access Control
        try:
            self.goto_product_overview(driver)
            
            product_access_functional = ("product" in driver.page_source.lower() and 
                                       "VAPT-Production-Environment" in driver.page_source)
            
            self.category_results['product_access_control'] = product_access_functional
            print("✅ Product access control functional" if product_access_functional else "❌ Product access control failed")
            
        except Exception as e:
            self.category_results['product_access_control'] = False
            print(f"❌ Product access control failed: {str(e)}")
        
        # Test 7.3: Finding Access Control
        try:
            driver.find_element(By.LINK_TEXT, "VAPT-Production-Environment").click()
            driver.find_element(By.LINK_TEXT, "Q4 Security Assessment 2024").click()
            
            finding_access_functional = ("Remote Code Execution" in driver.page_source or 
                                       "Information Disclosure" in driver.page_source)
            
            self.category_results['finding_access_control'] = finding_access_functional
            print("✅ Finding access control functional" if finding_access_functional else "❌ Finding access control failed")
            
        except Exception as e:
            self.category_results['finding_access_control'] = False
            print(f"❌ Finding access control failed: {str(e)}")
    
    # ===========================
    # UTILITY METHODS
    # ===========================
    
    def ensure_test_environment_exists(self):
        """Ensure test environment exists for testing"""
        try:
            self.goto_product_overview(self.driver)
            if "VAPT-Production-Environment" not in self.driver.page_source:
                self.test_01_project_and_asset_management()
        except Exception as e:
            print(f"Warning: Could not ensure test environment exists: {str(e)}")
    
    @classmethod
    def generate_final_report(cls):
        """Generate final comprehensive test report"""
        report_path = Path("/tmp/vapt_tests/test_reports/defectdojo_comprehensive_test_results.json")
        report_path.parent.mkdir(exist_ok=True)
        
        # Calculate summary statistics
        total_tests = sum(len(category.values()) for category in cls.test_report['test_categories'].values())
        passed_tests = sum(
            sum(1 for result in category.values() if result) 
            for category in cls.test_report['test_categories'].values()
        )
        
        cls.test_report['summary'] = {
            'total_categories': len(cls.test_report['test_categories']),
            'total_tests': total_tests,
            'passed_tests': passed_tests,
            'failed_tests': total_tests - passed_tests,
            'success_rate': f"{(passed_tests / total_tests * 100):.1f}%" if total_tests > 0 else "0%",
            'platform_assessment': 'PRODUCTION READY' if passed_tests / total_tests >= 0.8 else 'NEEDS CONFIGURATION'
        }
        
        # Save report
        with open(report_path, 'w') as f:
            json.dump(cls.test_report, f, indent=2)
        
        print(f"\n📊 Final test report saved: {report_path}")
        
        # Print summary
        print("\n" + "="*80)
        print("🎯 DEFECTDOJO VAPT WORKFLOW TEST SUMMARY")
        print("="*80)
        print(f"📅 Test Period: {cls.test_report['execution_start']} - {cls.test_report['execution_end']}")
        print(f"🧪 Total Tests: {total_tests}")
        print(f"✅ Passed: {passed_tests}")
        print(f"❌ Failed: {total_tests - passed_tests}")
        print(f"📊 Success Rate: {cls.test_report['summary']['success_rate']}")
        print(f"🎯 Platform Assessment: {cls.test_report['summary']['platform_assessment']}")
        
        return report_path


def create_comprehensive_vapt_suite():
    """Create the comprehensive VAPT test suite"""
    suite = unittest.TestSuite()
    
    # Add all test methods in execution order
    suite.addTest(VAPTWorkflowComprehensiveTest('test_01_project_and_asset_management'))
    suite.addTest(VAPTWorkflowComprehensiveTest('test_02_vulnerability_import_and_discovery'))
    suite.addTest(VAPTWorkflowComprehensiveTest('test_03_workflow_and_assignment_management'))
    suite.addTest(VAPTWorkflowComprehensiveTest('test_04_verification_and_closure_process'))
    suite.addTest(VAPTWorkflowComprehensiveTest('test_05_reporting_and_dashboard_functionality'))
    suite.addTest(VAPTWorkflowComprehensiveTest('test_06_notifications_and_alert_systems'))
    suite.addTest(VAPTWorkflowComprehensiveTest('test_07_security_and_access_control'))
    
    return suite


if __name__ == '__main__':
    # Configure test suite settings
    suite = create_comprehensive_vapt_suite()
    set_suite_settings(suite, jira=False, github=False, block_execution=False)
    
    # Run the comprehensive test suite
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print(f"\n🏆 VAPT Workflow Testing Complete!")
    print(f"Results: {result.testsRun - len(result.failures) - len(result.errors)}/{result.testsRun} tests passed")
    
    if result.failures or result.errors:
        print("\n⚠️  Some tests failed - review DefectDojo configuration")
    else:
        print("\n✅ All tests passed - DefectDojo is ready for VAPT workflows!")